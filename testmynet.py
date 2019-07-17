from argparse import ArgumentParser
from selenium import webdriver

class TestMyNet():

    def __init__(self, args):

        self.url = 'https://www.testmy.net'
        self.args = args
         
        #print('loading browser...')
        self.load_browser()
        
        if args.list:
            self.print_servers()
            exit()
           
        if args.server is not None:
            self.set_server(args.server)

        if not self.args.no_download:
            self.start_test(test_name='download')
            self.print_result()

        if not self.args.no_upload:
            self.start_test(test_name='upload')
            self.print_result()

        self.browser.quit()
        print('test successfully concluded')

    def load_browser(self):
        
        try:
            opts = webdriver.FirefoxOptions()
            opts.headless = True
            #self.browser = webdriver.Firefox(options=opts)
            self.browser = webdriver.Firefox()
        except:
            pass
        else:
            return

        try:
            self.browser = webdriver.Chrome()
        except:
            print('webdriver error')
            exit()
        else:
            return

    def start_test(self, test_name):

        print(f'testing {test_name} speed...')

        #self.browser.implicitly_wait(30)
        url = f'{self.url}/{test_name}'
        self.load_url(url)

        print(self.browser.find_elements_by_class_name('btn')[1])
        #elem_start = self.browser.find_elements_by_class_name('btn')[1]
        #elem_start.click()
        #bronken when choose a new server

    def load_url(self, url):

        try:
            self.browser.get(url)
        except:
            print('timeout error')
            self.browser.quit()
            exit()
        
    def get_servers(self):

        url = 'https://testmy.net/mirror'
        self.load_url(url)
        
        elems_servers = self.browser.find_elements_by_class_name('lead')
        z = zip(range(1, len(elems_servers)+1), elems_servers) 
        dict_servers = dict(z)
        return dict_servers

    def print_servers(self):
        
        servers = self.get_servers()
        for code, name in servers.items():
            print(f'{code} {name.text}')

    def set_server(self, code):

        servers = self.get_servers()
        try:
            servers[code].click()
        except KeyError:
            print('server code error')
            exit()
        
    def print_result(self):

        elem = self.browser.find_elements_by_class_name('highcharts-label')[0]
        print(elem.text)


def main():

    parser = ArgumentParser(#prog='testmynet',
                            description='A command line interface to test the internet speed using testmy.net',
                            epilog='See more on www.github.com/agenorgoncalvesneto/testmynet')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--no-download', action='store_true', default=False, help='do not perform donwload test')
    group.add_argument('-u', '--no-upload', action='store_true', default=False, help='do not perform upload test')
    parser.add_argument('--list', action='store_true', default=False, help='display a list of testmy.net servers')
    parser.add_argument('--server', metavar='', type=int, help='specify a server id to test against')
    #parser.add_argument('-q', '--quiet', action='store_true', default=False, help='show quiet output')
    #parser.add_argument('-v', '--verbose', action='store_true', default=False, help='show verbose output')
    args = parser.parse_args()
    TestMyNet(args)

if __name__ == '__main__':
    
    main()

