#!./venv/bin/python

from argparse import ArgumentParser
from selenium import webdriver

class TestMyNet():

    def __init__(self, args):
        ''' TestMyNet, ArgumentParse -> None '''

        self.url = 'https://www.testmy.net'
        self.args = args
        self.str_result = ''

        self.load_browser()

        if args.list:
            self.print_servers()
            self.browser.quit()
            exit()

        if args.server is not None:
            self.set_server(args.server)

        if not self.args.no_download:
            self.start_test(test_name='download')

        if not self.args.no_upload:
            self.start_test(test_name='upload')

        self.print_result()
        self.browser.quit()
        print('test successfully concluded')

    def load_browser(self):
        ''' TestMyNet -> None
        Tries to load the Firefox wedriver in path ./venv/bin/geckcriver
        Exits the program if a error is raised.
        '''
        try:
            opts = webdriver.FirefoxOptions()
            opts.headless = True
            self.browser = webdriver.Firefox(executable_path='./venv/bin/geckodriver' ,options=opts)
        except:
            print('webdriver error')
            exit()
        else:
            return

    def start_test(self, test_name):
        ''' TestMyNet, string -> None

        test_name: name of the test that will be performed (download or upload)
        '''
        
        print(f'testing {test_name} speed...')

        url = f'{self.url}/{test_name}'
        self.load_url(url)

        elem_start = self.browser.find_elements_by_class_name('button')[-1]
        elem_start.click()

        self.get_result(test_name)

    def load_url(self, url):
        ''' TestMyNet, string -> None

        url: URL that the webdriver will load
        '''

        try:
            self.browser.get(url)
        except:
            print('url load error')
            self.browser.quit()
            exit()

    def get_servers(self):
        ''' TestMyNet -> dict '''
        
        url = f'{self.url}/mirror'
        self.load_url(url)

        elems_servers = self.browser.find_elements_by_class_name('lead')
        z = zip(range(1, len(elems_servers)+1), elems_servers)
        dict_servers = dict(z)
        return dict_servers

    def print_servers(self):
        ''' TestMyNet -> None '''

        str_servers = ''
        servers = self.get_servers()
        for code, name in servers.items():
            code = str(code).rjust(2)
            str_servers += f'{code} {name.text}\n'
        print(str_servers)

    def set_server(self, code):
        ''' TestMyNet, string -> None

        code: server code according to https://testmy.net/mirror numbered from 1
        '''

        servers = self.get_servers()
        try:
            servers[code].click()
        except KeyError:
            print('server code error')
            self.browser.quit()
            exit()

    def get_server(self):
        ''' TestMyNet -> None '''

        current_server = self.browser.find_element_by_class_name('signin').text
        return current_server

    def get_result(self, test_name):
        ''' TestMyNet, string -> None

        Gets the test result.

        test_name: name of the test that was performed (download or upload)
        '''

        if test_name == 'download':
            elem = self.browser.find_element_by_class_name('color22')
        elif test_name == 'upload':
            elem = self.browser.find_element_by_class_name('color23')
        self.str_result += f' | {test_name} {elem.text}'

    def print_result(self):
        ''' TestMyNet -> None '''

        current_server = self.get_server()
        self.str_result = f'{current_server}{self.str_result}'
        print(self.str_result)


def main():

    parser = ArgumentParser(prog='testmynet',
                            description='A command line interface to test the internet speed using testmy.net',
                            epilog='See more on www.github.com/agenorgoncalvesneto/testmynet')
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--no-download', action='store_true',
                       default=False, help='do not perform donwload test')
    group.add_argument('-u', '--no-upload', action='store_true',
                       default=False, help='do not perform upload test')

    parser.add_argument('--list', action='store_true',
                        default=False, help='display a list of testmy.net servers and exit')
    parser.add_argument('--server', metavar='',
                        type=int, help='specify a server id to test against')
    #parser.add_argument('-q', '--quiet', action='store_true', default=False, help='show quiet output')
    #parser.add_argument('-v', '--verbose', action='store_true', default=False, help='show verbose output')
    args = parser.parse_args()
    TestMyNet(args)

if __name__ == '__main__':

    main()
