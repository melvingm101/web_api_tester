import re

def parse_x_powered_by(header_value: str):
    """
    If PHP is present, this function will parse the technology and the version.

    Args:
        header_value: The string value from the X-Powered-By header (e.g., 'PHP/8.2.1', 'Express').

    Returns:
        A tuple containing (technology_name, version_number).
        version_number will be None if no clear version is found.
    """

    # 1. Look for the common 'Technology/Version' format
    parts = header_value.split('/', 1)
    technology = parts[0].strip()

    if len(parts) == 2:
        # Check if the second part looks like a version number (contains digits and/or dots)
        version_part = parts[1].strip()
        if re.search(r'[\d.]', version_part):
            # Use regex to isolate the version number itself
            # This handles cases like 'PHP/8.2.1-fpm' and extracts only '8.2.1'
            version_match = re.search(r'^([\d.]+)', version_part)
            if version_match:
                return (technology, version_match.group(1))
            else:
                # If a '/' was used but the second part wasn't a standard version,
                # return the whole second part as the version
                return (technology, version_part)
        else:
            # If the second part doesn't look like a version (e.g., 'MyTech/CustomName'),
            # we'll return the technology only and None for the version
            pass

    # 2. Handle simple 'Technology' format (or if the above logic failed to find a clean version)
    return (technology, None)
