from .models import Contributors


def get_profile_picture(backend, user, response, details, *args, **kwargs):
	url = None
	profile = Contributors.objects.get_or_create(user = user)[0]
	if backend.name == 'facebook':
		profile.image = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
	elif backend.name == "twitter":
		if response['profile_image_url'] != '':
			if not response.get('default_profile_image'):
				avatar_url = response.get('profile_image_url_https')
				if avatar_url:
					avatar_url = avatar_url.replace('_normal.', '_bigger.')
					profile.image = avatar_url
	profile.save()