def is_clickjacking_possible(header_info):
    frame_list = ["SAMEORIGIN", "DENY"]
    if "X-Frame-Options" in header_info or "x-frame-options" in header_info:
        if header_info["X-Frame-Options"] in frame_list or header_info["x-frame-options"] in frame_list:
            return False
        else:
            return True
    
    if "UncommonHeaders" in header_info:
        if "content-security-policy" in header_info["UncommonHeaders"]:
            return False
    
    return True
