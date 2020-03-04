import datetime
from datetime import timedelta
import informix_conn
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
date=datetime.datetime(2019, 9, 5, 00, 00)
oneday=timedelta(days=1)
date2=date+oneday

q1="""
select
substr(round(date,'MI')::char(16),-5,5) as HHMI,
(value-lag(value) over (partition by name order by date))::int8  delta
from ifr_sysprofile 
where name = 'bufreads'
and date > ?
and date <= ? 
"""

def show_bufreads():
    X = []
    Y = []
    curs = _CONN.cursor()
    d1 = date.strftime('%Y-%m-%d %H:%M:%S')
    d2 = date2.strftime('%Y-%m-%d %H:%M:%S')

    curs.execute(q1,(d1,d2))
    for row in curs.fetchall():
        add_dot(X,Y,row)
    curs.close()
    ploting(X,Y)


def add_dot(X,Y,row):
	X.append(row[0])
	Y.append(row[1])
	plt.plot(X,Y)

def ploting(X,Y):
    xticks = []

    plt.ticklabel_format(style='plain')
    plt.axes().yaxis.grid()
    plt.rcParams["figure.figsize"] = (20, 10)
    plt.rcParams.update({'font.size': 15})
    plt.rcParams['lines.linewidth'] = 1
    ax = gca().xaxis
    six = [i for i in range(len(X)) if i % 6 == 0]
    for i in six:
        xticks.append(X[i])
    plt.xticks(xticks)
    print(max(i for i in Y if i is not None))
    plt.ylim(0,800000000)
    plt.tick_params(axis='x', labelsize=6)
    plt.tick_params(axis='y', labelsize=10)
    plt.title('BUFFER READS(page)')
    plt.savefig("./select_table.png", dpi=300)
    plt.show()

def main():
    """main"""
    try:
        global _CONN
        _CONN=informix_conn.init_db_conn(informix_conn.connect_string)
    except Exception as err:
        print(str(err))
    else:
        show_bufreads()
        _CONN.close()

if __name__ == '__main__':
        main()