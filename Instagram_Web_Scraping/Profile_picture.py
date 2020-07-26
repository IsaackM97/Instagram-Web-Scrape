import urllib.request
from bs4 import BeautifulSoup as bs


def get_profile_image():
    url = f'https://www.instagram.com/{user_name}/'
    print(f'Connecting to your profile {url}')
    try:
        response = urllib.request.urlopen(url).read()

        soup = bs(response, 'html.parser')

        meta = soup.find_all('meta', {'property': 'og:image'})  # gets the meta tag for property og:image (profile image)

        img_src = meta[0]['content']

        name = url.split('/')[-2]

        pic_name = f'{name}.jpg'

        urllib.request.urlretrieve(img_src, pic_name)

        print(f'Your downloaded image has been saved as {pic_name}')

    except:
        print(f"Cannot connect to '{user_name}'. Check if the username is spelled correctly.")


if __name__ == '__main__':
    user_name = input('Enter the username: ')
    get_profile_image()
