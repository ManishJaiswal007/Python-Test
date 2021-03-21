import most_used_ips as mi

file_name="test_access.log"

def test_top_client_ips():
    ips = mi.get_top_client_ips(file_name,10)
    assert len(ips)==10

