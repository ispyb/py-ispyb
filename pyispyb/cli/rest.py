from argparse import ArgumentParser
import enum
import json

from ..config import settings
from .requests import RestClient


class MethodEnum(enum.Enum):
    GET = "get"
    POST = "post"
    PUT = "put"
    PATCH = "patch"
    DELETE = "delete"


def run():
    parser = ArgumentParser(description="Use and display result from ISPyB REST API")
    parser.add_argument(
        "url",
        type=str,
        help="URL of the REST API. Can be a local url: /samples, or a fully qualified url: https://host:port/ispyb/v1/api/samples",
    )
    parser.add_argument(
        "-m",
        "--method",
        type=MethodEnum,
        default=MethodEnum.GET,
        help="HTTP method to use: get, post, put, patch, delete",
    )
    parser.add_argument("-l", "--login", type=str, default="abcd", help="Login to use")
    parser.add_argument(
        "-a", "--admin", action="store_true", help="Login as admin (efgh)"
    )
    parser.add_argument(
        "-d", "--data", type=str, help="Data to pass to the request as a json string"
    )
    parser.add_argument(
        "-r", "--api-root", type=str, default=settings.api_root, help="API root"
    )
    parser.add_argument(
        "-b", "--base-url", type=str, default="localhost", help="Base url"
    )
    parser.add_argument("-s", "--https", action="store_true", help="Use https")
    parser.add_argument(
        "-nv",
        "--no-verify",
        action="store_true",
        help="Dont verify https certificate, assume --https",
    )

    options = parser.parse_args()

    print("- Log-in to the service")
    _base_url = options.base_url + options.api_root
    url = options.url
    https = options.https
    port = None
    if options.url.startswith("http"):
        if options.url.startswith("https"):
            https = True

        parts = options.url.split("/")
        _base_url = parts[2]

        parts2 = _base_url.split(":")
        if len(parts2) == 2:
            _base_url = parts2[0]
            port = parts2[1]

        url = "/" + "/".join(parts[3:])

    base_url = f"{'https' if (https or options.no_verify) else 'http'}://{_base_url}"
    if options.no_verify:
        import urllib3

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    client = RestClient(base_url, port=port, verify=not options.no_verify)
    if not client.login("efgh" if options.admin else options.login, "a"):
        print("** Could not login **")
        exit(0)

    if url.startswith("/api"):
        url = url[4:]

    print("- Send request:")
    print(f"    method: {options.method.value}")
    print(f"    url   : {url}")

    data = None
    if options.data:
        try:
            data = json.loads(options.data)
            print(f"    data   : {options.data}")
        except json.JSONDecodeError as e:
            print("** Could not deseralise json data **")
            print(f"   {str(e)}")
            exit(0)

    print("-" * 80)
    client.req(url, method=options.method.value, data=data, pprint=True)
    print("-" * 80)

    print("- Terminated")


if __name__ == "__main__":
    run()
