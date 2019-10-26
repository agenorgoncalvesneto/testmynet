#!./venv/bin/python

from argparse import ArgumentParser
from selenium import webdriver

class TestMyNet():

    def __init__(self, args):

        self.url = 'https://www.testmy.net'
        self.str_result = ''

        self.load_browser()
        self.load_url('https://www.testmy.net/mirror')

        if args.list:
            self.print_servers()

        if args.server is not None:
            self.set_server(args.server)

        self.start_test(args.download, args.upload)

        self.print_result()
        self.browser.quit()
        print('test successfully concluded')


    def load_browser(self):
        """ Tries to load the Firefox wedriver in path ./venv/bin/geckcriver.
        Exits the program if a error is raised.
        """
        try:
            opts = webdriver.FirefoxOptions()
            #opts.headless = True
            self.browser = webdriver.Firefox(executable_path='./venv/bin/geckodriver', options=opts)
        except:
            print('Webdriver error')
            exit()


    def print_servers(self):
        """ Prints all servers listed in https://testmy.net/mirror and exits
        the program.
        """

        servers = self.browser.find_element_by_class_name('list-group')
        servers = servers.text.split('\n')
        servers = [s.strip() for s in servers] # Central US — Dallas, TX, USA
        servers = [s.split(' — ')[-1] for s in servers] # Dallas, TX, USA
        servers = [s.split(', ') for s in servers] # ['Dallas', 'TX', 'USA']
        servers = ['{}, {}'.format(s[0], s[-1]) for s in servers] # Dallas, USA

        for s in servers:
            code = str(servers.index(s))
            print('{} {}'.format(code.rjust(2), s))

        self.browser.quit()
        exit()


    def set_server(self, code):
        """ Sets the server to perform the tests against.

        Parameters
        ----------
        code : int
            Server code numbered from 1 according to testmy.net/mirror

        Raises
        ------
        IndexError
            If the code is not a valid server list index
        """

        try:
            servers = self.browser.find_elements_by_class_name('lead')
            servers[code].click()
        except IndexError:
            print('Server code error')
            self.browser.quit()
            exit()


    def start_test(self, download, upload):
        """ TestMyNet, string -> None

        test_name: name of the test that will be performed (download or upload)
        """

        buttons = self.browser.find_elements_by_class_name('btn')
        btn_download = buttons[0]
        btn_upload = buttons[1]
        btn_combined = buttons[2]

        if download:
            print('testing download speed...')
            btn_download.click()
        elif upload:
            print('testing upload speed...')
            btn_upload.click()
        else:
            print('testing download and upload speeds...')
            btn_combined.click()

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
    group.add_argument('-d', '--download', action='store_true',
                       default=False, help='performs only download test')
    group.add_argument('-u', '--upload', action='store_true',
                       default=False, help='performs only upload test')

    parser.add_argument('--list', action='store_true',
                        default=False, help='display a list of testmy.net servers and exit')
    parser.add_argument('--server', metavar='',
                        type=int, help='specify a server id to test against')
    #parser.add_argument('-q', '--quiet', action='store_true', default=False, help='show quiet output')
    #parser.add_argument('-v', '--verbose', action='store_true', default=False, help='show verbose output')

    ### ADD details

    args = parser.parse_args()
    TestMyNet(args)

if __name__ == '__main__':

    main()
