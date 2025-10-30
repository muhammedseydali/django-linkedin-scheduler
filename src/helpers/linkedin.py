import requests

from django.contrib.auth import get_user_model


class UserNotConnectedLinkedIn(Exception):
    pass


def get_linkedin_user_details(user):
    try:
        linkedin_social = user.socialaccount_set.get(provider="linkedin")
    except:
        raise UserNotConnectedLinkedIn("LinkedIn is not connected on this user.")
    return linkedin_social

def get_share_headers(linkedin_social):
    tokens = linkedin_social.socialtoken_set.all()
    if not tokens.exists():
        raise Exception("LinkedIn connection is invalid. Please login again.")
    social_token = tokens.first()
    return {
        "Authorization": f"Bearer {social_token.token}",
        "X-Restli-Protocol-Version": "2.0.0"
    }



def post_to_linkedin(user, text: str):
    try:
        User = get_user_model()
        if not isinstance(user, User):
            raise TypeError("Invalid user instance")

        linkedin_social = get_linkedin_user_details(user)
        linkedin_user_id = linkedin_social.uid if linkedin_social else None
        if not linkedin_user_id:
            raise ValueError("Invalid or missing LinkedIn User ID")

        headers = get_share_headers(linkedin_social)
        endpoint = "https://api.linkedin.com/v2/ugcPosts"

        payload = {
            "author": f"urn:li:person:{linkedin_user_id}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": text},
                    "shareMediaCategory": "NONE",
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            },
        }

        response = requests.post(endpoint, json=payload, headers=headers)

        # Raise HTTPError for bad responses (4xx, 5xx)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error while posting to LinkedIn: {http_err}")
        raise Exception("LinkedIn API returned an error")

    except requests.exceptions.RequestException as req_err:
        print(f"Network or request error: {req_err}")
        raise Exception("Network error — please check your internet connection or API availability")

    except (TypeError, ValueError) as val_err:
        print(f"Validation error: {val_err}")
        raise Exception(str(val_err))

    except Exception as e:
        print(f"Unexpected error: {e}")
        raise Exception("An unexpected error occurred while posting to LinkedIn")
