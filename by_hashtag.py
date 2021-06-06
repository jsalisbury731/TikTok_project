import pandas as pd
from TikTokApi import TikTokApi

verifyFp = "verify_7d2989b7e9d41d606a7e16750e49379c"
api = TikTokApi.get_instance(custom_verifyFp=verifyFp)


hashtag = 'money'
n_count = 10

hashtag_pull = api.by_hashtag(hashtag = hashtag, count = n_count)

def simple_dict(tiktok_dict):
  to_return = {}
  to_return['user_name'] = tiktok_dict['author']['uniqueId']
  to_return['user_id'] = tiktok_dict['author']['id']
  to_return['nickname'] = tiktok_dict['author']['nickname']
  to_return['video_id'] = tiktok_dict['id']
  to_return['video_desc'] = tiktok_dict['desc']
  to_return['video_time'] = tiktok_dict['createTime']
  to_return['video_length'] = tiktok_dict['video']['duration']
  to_return['video_link'] = 'https://www.tiktok.com/@{}/video/{}?lang=en'.format(to_return['user_name'], to_return['video_id'])
  to_return['n_likes'] = tiktok_dict['stats']['diggCount']
  to_return['n_shares'] = tiktok_dict['stats']['shareCount']
  to_return['n_comments'] = tiktok_dict['stats']['commentCount']
  to_return['n_plays'] = tiktok_dict['stats']['playCount']
  return to_return




videos = [simple_dict(v) for v in hashtag_pull]
videos_df = pd.DataFrame(videos)


# print(videos_df)

videos_df.to_csv(f'hashtag_{hashtag}.csv', index=False)