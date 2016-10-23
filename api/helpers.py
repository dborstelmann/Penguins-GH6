

def add_unique_demographics_to_profile(profile):
    if "woman" in profile and "family" in profile:
        profile.add("woman_with_child")

    return profile
