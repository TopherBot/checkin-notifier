import json
from unittest import mock

from checkin_notifier import send

@mock.patch("requests.post")
def test_post_message_success(mock_post):
    mock_resp = mock.Mock()
    mock_resp.raise_for_status.return_value = None
    mock_post.return_value = mock_resp

    url = "https://example.com/webhook"
    txt = "hello"
    send.post_message(url, txt)

    mock_post.assert_called_once()
    args, kwargs = mock_post.call_args
    assert args[0] == url
    assert json.loads(kwargs["data"]) == {"text": txt}
    assert kwargs["headers"] == {"Content-Type": "application/json"}
