import pandas as pd
from TikTokApi import TikTokApi

verifyFp="verify_7d2989b7e9d41d606a7e16750e49379c"
api = TikTokApi.get_instance(custom_verifyFp=verifyFp)

filename = './csv/hashtag_affiliatemarketing.csv'

df = pd.read_csv(filename)

hashtag_used = filename[6:-4]

user_list = list(set(df.user_name))
print(f'Total unique users: {len(user_list)}.')


def user_dict(tiktok_dict):
  to_return = {}
  to_return['video_id'] = tiktok_dict['id']
  to_return['description'] = tiktok_dict['desc']
  to_return['creation_time'] = tiktok_dict['createTime']
  to_return['duration'] = tiktok_dict['video']['duration']
  to_return['author_id'] = tiktok_dict['author']['id']
  to_return['username'] = tiktok_dict['author']['uniqueId']
  to_return['nickname'] = tiktok_dict['author']['nickname']
  to_return['music_id'] = tiktok_dict['music']['id']
  to_return['song_title'] = tiktok_dict['music']['title']
  to_return['music_author_name'] = tiktok_dict['music']['authorName']
  # to_return['music_duration'] = tiktok_dict['music']['duration']
  # to_return['challenge_id'] = tiktok_dict['challenges'][0]['id']
  # to_return['challenge_title'] = tiktok_dict['challenges'][0]['title']
  to_return['diggs'] = tiktok_dict['stats']['diggCount']
  to_return['shares'] = tiktok_dict['stats']['shareCount']
  to_return['comments'] = tiktok_dict['stats']['commentCount']
  to_return['plays'] = tiktok_dict['stats']['playCount']
  return to_return


# #######################
n_count = 2000
# #######################

users_videos = []

for author in user_list:
  print(author)
  user_videos_pull = api.by_username(username=author, count=n_count)
  users_videos_temp = [user_dict(v) for v in user_videos_pull]
  for video in users_videos_temp:
    users_videos.append(video)

  print(len(users_videos))

users_videos_df = pd.DataFrame(users_videos)


users_videos_df.to_csv(f'./csv/users_videos_{hashtag_used}_{str(pd.Timestamp.now())[:19].replace(":", "-")}.csv', index=False)