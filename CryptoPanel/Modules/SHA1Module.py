from CryptoPanel.Modules.HashModuleUtils import *

properties = {
    'name': 'SHA1',
    'categories': '校验',
    'input': {0: '输入'},
    'output': {0: '输出'},
    'properties': {
        'salt长度': str,
        'eval': bool
    }
}

defaults = {
    'salt长度': '0',
    'eval': False
}


def main(inp, settings):
    if settings['eval'] == True:
        inps = eval(inp[0])
    else:
        inps = inp[0].encode()
    salt = int(settings['salt长度'])
    print(inp[0], salt)
    out = {0: str(generate_sha1(inps, salt))}
    return out
