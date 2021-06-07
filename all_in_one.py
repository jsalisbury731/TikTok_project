import pandas as pd
from TikTokApi import TikTokApi

verifyFp = "verify_7d2989b7e9d41d606a7e16750e49379c"
api = TikTokApi.get_instance(custom_verifyFp=verifyFp)


def hashtag_dict(tiktok_dict):
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


def user_video(tiktok_dict):
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
  try:
    to_return['music_author_name'] = tiktok_dict['music']['authorName']
  except:
    to_return['music_author_name'] = '-'
  # to_return['music_duration'] = tiktok_dict['music']['duration']
  # to_return['challenge_id'] = tiktok_dict['challenges'][0]['id']
  # to_return['challenge_title'] = tiktok_dict['challenges'][0]['title']
  to_return['diggs'] = tiktok_dict['stats']['diggCount']
  to_return['shares'] = tiktok_dict['stats']['shareCount']
  to_return['comments'] = tiktok_dict['stats']['commentCount']
  to_return['plays'] = tiktok_dict['stats']['playCount']
  return to_return


def user_detail(tiktok_dict):
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
  try:
    to_return['bio_link'].append(tiktok_dict['userInfo']['user']['bioLink']['link'])
  except:
    to_return['bio_link'].append('-')
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


#######################
hashtag = 'magiclinks'
htag_vid_count = 15
user_vid_count = 2000
offset = 0
#######################

# Pull videos by hashtag via API
hashtag_pull = api.by_hashtag(hashtag = hashtag, count = htag_vid_count, offset = offset)
# Run videos through hashtag_dict function
hashtag_videos = [hashtag_dict(v) for v in hashtag_pull]
# Create a dataframe for the hashtag videos
videos_df = pd.DataFrame(hashtag_videos)
# Output data frame to CSV
videos_df.to_csv(f'./csv/hashtag_{hashtag}_{str(pd.Timestamp.now())[:19].replace(":", "_")}.csv', index=False)
print('Hashtag videos saved to CSV.')

# Create list of unique users from hashtag videos
user_list = list(set(videos_df.user_name))
# Create an empty list to append to
users_videos = []
# Pull all videos for each author, append to users_videos list
for author in user_list:
  # print(author)
  user_videos_pull = api.by_username(username=author, count=user_vid_count)
  users_videos_temp = [user_video(v) for v in user_videos_pull]
  for video in users_videos_temp:
    users_videos.append(video)
# Convert users_videos list to a dataframe
users_videos_df = pd.DataFrame(users_videos)
# Output users_videos_df to CSV
users_videos_df.to_csv(f'./csv/users_videos_{hashtag}_{str(pd.Timestamp.now())[:19].replace(":", "_")}.csv', index=False)
print('Users videos saved to CSV.')


# Create an empty list to append to
users_details_list = []
# Pull all details for each author, append to users_details_list
for author in user_list:
  # print(author)
  user_detail_pull = api.get_user(username=author)
  users_details = user_detail(user_detail_pull)
  users_details_list.append(users_details)
# Convert users_details_list to a dataframe
users_details_df = pd.DataFrame(users_details_list)
# Output users_details_df to CSV
users_details_df.to_csv(f'./csv/get_user_details_{hashtag}_{str(pd.Timestamp.now())[:19].replace(":", "_")}.csv', index=False)
print('Users details saved to CSV.')