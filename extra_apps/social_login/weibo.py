# coding:utf-8
# author:hepochen@gmail.com  https://github.com/hepochen
"""
Weibo OAuth2 backend, docs at:
    https://python-social-auth.readthedocs.io/en/latest/backends/weibo.html
"""
from social_core.backends.oauth import BaseOAuth2


class WeiboOAuth2(BaseOAuth2):
    """Weibo (of sina) OAuth authentication backend"""
    name = 'weibo'
    ID_KEY = 'uid'
    AUTHORIZATION_URL = 'https://api.weibo.com/oauth2/authorize'
    REQUEST_TOKEN_URL = 'https://api.weibo.com/oauth2/request_token'
    ACCESS_TOKEN_URL = 'https://api.weibo.com/oauth2/access_token'
    ACCESS_TOKEN_METHOD = 'POST'
    REDIRECT_STATE = False

    # usersocialauth 表存储的额外数据
    EXTRA_DATA = [
        ('id', 'id'),
        ('name', 'nickname'),
        ('avatar_large', 'avatar_large'),
        ('avatar_hd', 'avatar_hd'),
        ('profile_image_url', 'profile_image_url'),
        ('description', 'signature'),
        ('cover_image_phone', 'cover_image_phone'),
        ('created_at', 'created_at')
    ]

    def get_user_details(self, response):
        """Return user details from Weibo. API URL is:
        https://api.weibo.com/2/users/show.json/?uid=<UID>&access_token=<TOKEN>
        """
        nickname = response.get('name') or response.get('screen_name','')
        nickname = nickname[:20]

        email = (response.get('uid') or response.get('id')) + '@sina-social.com'
        image = response.get('image') or response.get('profile_image_url', 'Avatar/default.png')
        gender = 0 if(response.get('gender','m')=='m') else 1
        province = int(response.get('province', 0))
        city = int(response.get('city', 0))
        address = response.get('location', '')
        signature = response.get('description', '')[:40]

        return {'email': email,
                'nickname': nickname,
                'image':image,
                'gender': gender,
                'province': province,
                'city':city,
                'address':address,
                'signature':signature,
                }

    def get_uid(self, access_token):
        """Return uid by access_token"""
        data = self.get_json(
            'https://api.weibo.com/oauth2/get_token_info',
            method='POST',
            params={'access_token': access_token}
        )
        return data['uid']

    def get_email(self, access_token):
        data = self.get_json(
            'https://api.weibo.com/2/account/profile/email.json',
            method='GET',
            params={'access_token': access_token}
        )
        return data['email']

    def user_data(self, access_token, response=None, *args, **kwargs):
        """Return user data"""
        # If user id was not retrieved in the response, then get it directly
        # from weibo get_token_info endpoint
        uid = response and response.get('uid') or self.get_uid(access_token)
        user_data = self.get_json(
            'https://api.weibo.com/2/users/show.json',
            params={'access_token': access_token, 'uid': uid}
        )
        user_data['uid'] = uid
        return user_data
