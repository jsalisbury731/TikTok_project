import pandas as pd
from TikTokApi import TikTokApi

verifyFp="verify_7d2989b7e9d41d606a7e16750e49379c"
api = TikTokApi.get_instance(custom_verifyFp=verifyFp)


def user_dict(tiktok_dict):
  to_return = {}
  to_return['user_name'] = []
  to_return['user_name'].append(tiktok_dict['userInfo']['user']['uniqueId'])
  to_return['user_id'] = []
  to_return['user_id'].append(tiktok_dict['userInfo']['user']['id'])
  to_return['nickname'] = []
  to_return['nickname'].append(tiktok_dict['userInfo']['user']['nickname'])
  to_return['account_created'] = []
  to_return['account_created'].append(tiktok_dict['userInfo']['user']['createTime'])
  to_return['verified'] = []
  to_return['verified'].append(tiktok_dict['userInfo']['user']['verified'])
  to_return['bio_link'] = []
  to_return['bio_link'].append(tiktok_dict['userInfo']['user']['bioLink']['link'])
  to_return['followers'] = []
  to_return['followers'].append(tiktok_dict['userInfo']['stats']['followerCount'])
  to_return['following'] = []
  to_return['following'].append(tiktok_dict['userInfo']['stats']['followingCount'])
  to_return['heart'] = []
  to_return['heart'].append(tiktok_dict['userInfo']['stats']['heart'])
  to_return['heart_count'] = []
  to_return['heart_count'].append(tiktok_dict['userInfo']['stats']['heartCount'])
  to_return['videos'] = []
  to_return['videos'].append(tiktok_dict['userInfo']['stats']['videoCount'])
  to_return['diggs'] = []
  to_return['diggs'].append(tiktok_dict['userInfo']['stats']['diggCount'])
  return to_return


username = 'therock'

user_detail_pull = api.get_user(username = username)



output = user_dict(user_detail_pull)
print(type(output))

output_df = pd.DataFrame.from_dict(output)

print(output_df)


# videos = [user_dict(v) for v in user_detail_pull]
# videos_df = pd.DataFrame.from_dict(output)
#
#
# print(videos_df)
#
output_df.to_csv(f'./csv/get_user_{username}.csv', index=False)