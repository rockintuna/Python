from setuptools import setup
import informix_conn

def sum(a,b):
    return a+b

def main():
    """main"""
    print(informix_conn.connect_string)
    a=sum(1,2)
    print(a)

if __name__ == '__main__':
        main()