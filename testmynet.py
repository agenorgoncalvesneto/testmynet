from argparse import ArgumentParser
from selenium import webdriver

class TestMyNet():

    def __init__(self, args):

        self.url = 'https://www.testmy.net'
        self.args = args
         
        #print('loading browser...')
        self.load_browser()
        
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
            self.browser = webdriver.Firefox(options=opts)
            #self.browser = webdriver.Firefox()
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

        url = f'{self.url}/{test_name}'
        self.load_site(url)

        elem_start = self.browser.find_elements_by_class_name('btn')[1]
        elem_start.click()

    def load_site(self, url):

        #self.browser.implicitly_wait(self.args.timeout)
        try:
            self.browser.get(url)
        except:
            print('timeout error')
            self.browser.quit()
            exit()
        
    def print_result(self):
        elem = self.browser.find_elements_by_class_name('highcharts-label')[0]
        print(elem.text)

def main():

    parser = ArgumentParser(prog='testmynet',
                            description='A command line interface to test the internet speed using testmy.net',
                            epilog='See more on www.github.com/agenorgoncalvesneto/testmynet')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-d', '--no-download', action='store_true', default=False, help='do not perform donwload test')
    group.add_argument('-u', '--no-upload', action='store_true', default=False, help='do not perform upload test')
    #parser.add_argument('-q', '--quiet', action='store_true', default=False, help='show quiet output')
    #parser.add_argument('-v', '--verbose', action='store_true', default=False, help='show verbose output')
    args = parser.parse_args()
    TestMyNet(args)

if __name__ == '__main__':
    
    main()

