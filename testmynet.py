#!./venv/bin/python

from argparse import ArgumentParser

from selenium import webdriver


class Testmynet():
    """A class to perform download and upload tests using testmy.net.

    Atributes
    ---------
    self.browser : webdriver
        Webdriver used to navegate in testmy.net
    self.server : str
        Name of server that perform the tests

    Methods
    -------
    get_server()
        Gets the server that will be performed test against and set it
        in the class parameter self.server.
    load_browser()
        Tries to load the Firefox wedriver in path
        ./venv/bin/geckcriver.
    print_details()
        Prints the details of the test performed available at
        testmy.net.
    print_result()
        Prints the result after perform the tests. The prints follow the
        model 'Server | Download xMbps | Upload xMbps'.
    print_servers()
        Prints all servers listed in https://testmy.net/mirror and
        exits the program.
    start_test()
        Starts the download or upload test. Performs both tests if the
        parameters only_download and only_upload are False.
    set_server()
        Sets the server to perform the tests against.
    """

    def __init__(self, args):
        """Executes the workflow calling the others methods.

        Parameters
        ----------
        args : ArgumentParser
            Arguments to execute the program: download(bool), upload
            (bool), details(bool), list(bool) and server(int).
        """

        self.load_browser()

        if args.list:
            self.print_servers()

        if args.server is not None:
            self.set_server(args.server)

        self.get_server()
        self.start_test(args.download, args.upload)
        self.print_result()

        if args.details:
            self.print_details()

        self.browser.quit()

    def get_server(self):
        """Gets the server that will be performed test against and set
        it in the class parameter self.server.
        """

        server = self.browser.find_element_by_class_name('im-star')
        server = server.find_element_by_xpath('..')
        server = server.text
        server = server.strip()  # Central US — Dallas, TX, USA
        server = server.split(' — ')[-1]  # Dallas, TX, USA
        server = server.split(', ')  # ['Dallas', 'TX', 'USA']
        server = '{}, {}'.format(server[0], server[-1])  # Dallas, USA
        self.server = server

    def load_browser(self):
        """Tries to load the Firefox wedriver in path
        ./venv/bin/geckcriver.

        Raises
        ------
            Exits the program if any error is raised
        """

        try:
            opts = webdriver.FirefoxOptions()
            opts.headless = True
            self.browser = webdriver.Firefox(
                executable_path='./venv/bin/geckodriver',
                options=opts)
            self.browser.get('https://www.testmy.net/mirror')
        except:
            print('Error: webdriver')
            exit()

    def print_details(self):
        """Prints the details of the test performed available at
        testmy.net.
        """
        
        button = self.browser.find_element_by_id('share-tab')
        button.click()

        details = self.browser.find_element_by_class_name('form-control')
        details = details.text
        print('\n{}'.format(details))

    def print_result(self):
        """Prints the result after perform the tests. The prints follow
        the model 'Server | Download xMbps | Upload xMbps'.
        """

        result = self.server
        try:
            download = self.browser.find_element_by_class_name('color22')
            result += ' | Download {}'.format(download.text)
        except:
            pass

        try:
            upload = self.browser.find_element_by_class_name('color23')
            result += ' | Upload {}'.format(upload.text)
        except:
            pass

        result += '\nTest successfully concluded.'

        print(result)

    def print_servers(self):
        """Prints all servers listed in https://testmy.net/mirror and
        exits the program.
        """

        servers = self.browser.find_element_by_class_name('list-group')
        servers = servers.text.split('\n')
        servers = [s.strip() for s in servers]  # Central US — Dallas, TX, USA
        servers = [s.split(' — ')[-1] for s in servers]  # Dallas, TX, USA
        servers = [s.split(', ') for s in servers]  # ['Dallas', 'TX', 'USA']
        servers = ['{}, {}'.format(s[0], s[-1]) for s in servers]  # Dallas, USA

        for s in servers:
            code = str(servers.index(s))
            print('{} {}'.format(code.rjust(2), s))

        self.browser.quit()
        exit()

    def start_test(self, only_download, only_upload):
        """Starts the download or upload test. Performs both tests if
        the parameters only_download and only_upload are False.

        Parameters
        ----------
        only_download : bool
            If True only performs download speed test
        only_upload : bool
            If True only performs upload speed upload test
        """

        btns = self.browser.find_elements_by_class_name('btn')
        btn_download = btns[0]
        btn_upload = btns[1]
        btn_combined = btns[2]

        if only_download:
            print('Testing download speed...')
            btn_download.click()
        elif only_upload:
            print('Testing upload speed...')
            btn_upload.click()
        else:
            print('Testing download and upload speeds...')
            btn_combined.click()

    def set_server(self, code):
        """Sets the server to perform the tests against.

        Parameters
        ----------
        code : int
            Server code numbered from 0 according to testmy.net/mirror

        Raises
        ------
        IndexError
            If the code is not a valid server list index
        """

        try:
            servers = self.browser.find_elements_by_class_name('lead')
            servers[code].click()
        except IndexError:
            print('Error: Server code')
            self.browser.quit()
            exit()


if __name__ == '__main__':

    parser = ArgumentParser(
        prog='Testmynet',
        description="""A command line interface to test the internet speed
                    using testmy.net""",
        epilog='See more on www.github.com/agenorgoncalvesneto/testmynet')

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        '-d', '--download',
        action='store_true',
        default=False,
        help='performs only download test')

    group.add_argument(
        '-u', '--upload',
        action='store_true',
        default=False,
        help='performs only upload test')

    parser.add_argument(
        '--details',
        action='store_true',
        default=False,
        help='show the details after perform the tests')

    parser.add_argument(
        '--list',
        action='store_true',
        default=False,
        help='display a list of testmy.net servers and exit')

    parser.add_argument(
        '--server',
        metavar='',
        type=int,
        help='specify a server code to test against')

    args = parser.parse_args()
    Testmynet(args)
