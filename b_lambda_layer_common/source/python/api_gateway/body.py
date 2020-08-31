import base64
import json
import urllib.parse
from json import JSONDecodeError
from typing import Dict, Any


class Body:
    """
    Class dedicated to parsing API Gateway formed event bodies sent to Lambda functions.
    """

    def __init__(self, event: Dict[str, Any]):
        """
        Constructor.

        :param event: Lambda event.
        """
        self.__body = event['body']
        self.__is_base_64_encoded = event.get('isBase64Encoded', False)

    def from_urlencoded(self) -> Dict[str, Any]:
        """
        Loads a urlencoded body as a dictionary.

        :return: Event body as a dictionary.
        """
        str_body = self.decoded()
        parsed_body = {}

        for item in str_body.split('&'):
            key, value = item.split('=')
            parsed_value = urllib.parse.unquote(value)
            try:
                parsed_body[key] = json.loads(parsed_value)
            except JSONDecodeError:
                parsed_body[key] = parsed_value

        return parsed_body

    def from_json(self) -> Dict[str, Any]:
        """
        Loads a JSON body as a dictionary.

        :return: Event body as a dictionary.
        """
        return json.loads(self.decoded())

    def decoded(self) -> str:
        """
        Makes sure the body is not Base64 encoded.

        :return: Event body in string format.
        """
        if self.__is_base_64_encoded:
            return base64.b64decode(self.__body).decode()

        return self.__body
