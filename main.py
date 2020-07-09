import datetime, os

def logger(path):

    file_path = os.path.join(path, 'log.txt')
    info = {}
    
    def decorator(old_func):
        def new_function(*args, **kwargs):

            nonlocal info
            date_info = datetime.datetime.today().strftime('%d-%m-%Y, %I:%M')
            result = old_func(*args, **kwargs)
            info['function_name'] = old_func.__name__
            info['args'] = args
            info['date'] = date_info
            info['result'] = result
            with open(file_path, 'a', encoding='utf8') as fo:
                fo.write(str(info)+'\n')
            print(info)
            return result

        return new_function

    return decorator

@logger('C:\\Homework\\log\\')
def foo(a, b):
    return a * a + b

if __name__ == '__main__':
    print(foo(12, 151))