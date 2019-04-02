import tkinter as tk
import time


# SORTING ALGORITHMS

# BUBBLE SORT
def bubsort(l):
    last = len(l)
    swapped = True
    while swapped:
        swapped = False
        for j in range(1, last):
            if l[j - 1] > l[j]:
                l[j], l[j - 1] = l[j - 1], l[j]
                swapped = True
                last = j
                yield l


# INSERTION SORT
def insort(l):
    for i in range(1, len(l)):
        curval = l[i]
        pos = i
        while pos > 0 and l[pos - 1] > curval:
            l[pos] = l[pos - 1]
            pos -= 1
            yield l
        l[pos] = curval
        yield l


# SELECTION SORT
def selsort(l):
    for i in range(len(l)):
        min_idx = i
        for j in range(i + 1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
                root.update()
                root.after(slider.get())
        l[i], l[min_idx] = l[min_idx], l[i]
        yield l


# MERGE SORT
def merge_sort(arr):
    n = len(arr) - 1
    count = 1
    begin = 0
    end = 0
    while count <= n:
        while end < n:
            mid = begin + count // 2
            end = begin + count
            if (begin < n) and (end <= n):
                yield from merge(arr, begin, mid, end)
                begin = end + 1
            else:
                yield from merge(arr, begin - count - 1, begin - 1, n)
        count = 2 * count + 1
        begin = 0
        end = 0


# Merge Function
def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    left = [0] * n1
    right = [0] * n2
    for i in range(0, n1):
        left[i] = a[l + i]
    for i in range(0, n2):
        right[i] = a[m + i + 1]
    i, j, kay = 0, 0, l
    while i < n1 and j < n2:
        if left[i] > right[j]:
            a[kay] = right[j]
            j += 1
        else:
            a[kay] = left[i]
            i += 1
        kay += 1
        yield a
    while i < n1:
        a[kay] = left[i]
        i += 1
        kay += 1
        yield a
    while j < n2:
        a[kay] = right[j]
        j += 1
        kay += 1
        yield a


# HEAP SORT
def heap_sort(l):
    n = len(l)
    yield from buildMaxHeap(l, n)
    for i in range(n - 1, 0, -1):
        l[0], l[i] = l[i], l[0]
        yield l
        j, index = 0, 0
        while True:
            index = 2 * j + 1
            if (index < (i - 1) and
                    l[index] < l[index + 1]):
                index += 1
            if index < i and l[j] < l[index]:
                l[j], l[index] = l[index], l[j]
                yield l
            j = index
            if index >= i:
                break


# Build Heap
def buildMaxHeap(l, n):
    for i in range(n):
        if l[i] > l[int((i - 1) / 2)]:
            j = i
            while l[j] > l[int((j - 1) / 2)]:
                (l[j],
                 l[int((j - 1) / 2)]) = (l[int((j - 1) / 2)],
                                         l[j])
                j = int((j - 1) / 2)
                yield l


# QUICK SORT
def quick_sort(l, left, right):
    if left >= right:
        return
    pivot_idx = left
    old_r = right
    pivot = l[left]
    left += 1
    while True:
        # manual check, does it work when l=pivot_idx, r=l+1 for a[l] <= a[r], and for a[l] > a[r] ?
        while l[right] > pivot:
            right -= 1
        if left >= right:
            break
        while left < right and l[left] <= pivot:
            left += 1
        # pre-conditions to swap: l == r, or a[l] > pivot from 2nd loop, and a[r] <= pivot from 1st loop
        l[left], l[right] = l[right], l[left]
        yield l
    l[pivot_idx], l[right] = l[right], l[pivot_idx]
    yield l
    yield from quick_sort(l, pivot_idx, right)
    yield from quick_sort(l, right + 1, old_r)


sort_dic = {
    "bubble": bubsort,
    "insertion": insort,
    "selection": selsort,
    "merge": merge_sort,
    "heap": heap_sort,
    "quick": lambda l: quick_sort(l, 0, len(l) - 1)
}

# GUI
root = tk.Tk()
root.config(bg='#9400d3')
root.title('Sorting Visualizer')
root.geometry('700x700+400+50')

row1 = tk.Frame(root, bg='red', bd=5, relief='groove')

tk.Label(row1, text='SIZE OF ARRAY:', fg='yellow', bg='green', font=('courier', 20, 'bold')).pack(side="left")
e = tk.Entry(row1, bg='green', relief='raised', bd=2, fg='white', justify='center', font=('courier', 20, 'bold'))
e.pack(side="right", expand=True)

row2 = tk.Frame(root, bg='red', bd=5, relief='groove')

tk.Label(row2, text='SORTING ALGORITHM:', font=('courier', 20, 'bold'), fg='yellow', bg='green').pack(side="left")
choice = tk.StringVar(row2)
menu = tk.OptionMenu(row2, choice, *sorted(sort_dic.keys()))
menu.config(fg='white', bg='green', font=('courier', 20, 'bold'), highlightbackground='orange',
            activebackground='yellow')
choice.set("selection")
menu.pack(side="right")

row3 = tk.Frame(root, bg='red', bd=5, relief='groove')

tk.Label(row3, text='TIME PER OPERATION(ms):', fg='yellow', bg='green', font=('courier', 20, 'bold')).pack(
    side="left")
slider = tk.Scale(row3, from_=1, to=1000, orient='horizontal', fg='white', bg='green', font=('courier', 20, 'bold'),
                  troughcolor='orange', activebackground='yellow', highlightbackground='orange')
slider.set(100)
slider.pack(side="right", fill='x', expand=True)

row4 = tk.Frame(root, bd=5, relief='sunken')
lbl = tk.Label(row4, text='Iterations: %d' % 0, fg='#adff2f', font=('courier', 20, 'italic'), bd=5, bg='#c776b9',
               relief='raised')
lb = tk.Label(row4, text='START', fg='#adff2f', font=('courier', 20, 'italic'), bd=5, bg='#c776b9', relief='raised')
lbr = tk.Label(row4, text='Time: %f' % 0, fg='#adff2f', font=('courier', 20, 'italic'), bd=5, bg='#c776b9',
               relief='raised')

c = tk.Canvas(root, bg='#ADFF2F')


def visualize(l):
    n = len(l)
    cw = c.winfo_width()
    ch = c.winfo_height()
    rh = ch * 9 / 10
    th = ch * 19 / 20
    for i in range(n):
        height = l[i] * rh / n
        c.create_rectangle(i * cw / n, rh - height, (i + 1) * cw / n, rh, fill="green")
        c.create_text((i + 0.5) * cw / n, th, text=str(l[i]))


stopped = False
paused = False

k = 0


def prompt():
    win = tk.Toplevel()
    win.wm_title("ERROR!!")
    win.geometry('500x100')
    win.config(background='white')

    def animate():
        global k
        if k % 2 == 0:
            win.config(background='black')
            pl.config(fg='yellow', bg='red')
        else:
            win.config(background='white')
            pl.config(fg='red', bg='yellow')
        k += 1
        win.after(250, animate)

    pl = tk.Label(win, text="GIVE POSITIVE INTEGER INPUT!", fg='red', bg='yellow', font=('courier', 20, 'bold'),
                  relief='groove',
                  bd=10)
    animate()
    pl.pack()
    tk.Button(win, text="Okay", command=win.destroy, fg='yellow', bg='orange', font=('courier', 20, 'bold'),
              relief='groove',
              bd=10).pack()


def start():
    global c, stopped, paused

    stopped = False
    paused = False

    steps = 0
    zero = time.time()
    pause_zero = 0.0

    root.update()
    c.delete("all")
    lb.config(text="this is the array")
    lbl.config(text="Iterations: %d" % steps)
    lbr.config(text="Time: %d" % 0.0)

    try:
        n = int(e.get())
    except:
        prompt()
        return

    sl = [i for i in range(n, 0, -1)]

    visualize(sl)
    root.update()
    root.after(2000)
    root.update()

    lb.config(text="sorting")

    g = sort_dic[choice.get()](sl)

    for l_iter in g:
        c.delete("all")
        visualize(l_iter)
        steps += 1
        lbl.config(text="Iterations: %d" % steps)
        lbr.config(text="Time: %f" % (time.time() - zero))
        root.after(slider.get())
        root.update()
        if paused:
            pause_zero = time.time()
        while paused:
            root.update()
            if stopped:
                break
            if not paused:
                zero += time.time() - pause_zero

        if stopped:
            c.delete("all")
            break

    if not stopped:
        lb.config(text="sorted!")
        stopped = True


def pause():
    global paused, pause_button
    if stopped:
        return
    if paused:
        paused = False
        lb.config(text="sorting")
        pause_button.config(text='PAUSE')
    else:
        paused = True
        lb.config(text="paused")
        pause_button.config(text='CONTINUE')


def stop():
    global stopped
    stopped = True
    lb.config(text="stopped")
    pause_button.config(text='PAUSE')


buttons = tk.Frame(root, bg='red', bd=5, relief='groove')
start_button = tk.Button(buttons, text='GO', command=start, fg='yellow', bg='orange', font=('courier', 20, 'bold'),
                         relief='groove',
                         bd=10)
pause_button = tk.Button(buttons, text='PAUSE', command=pause, fg='yellow', bg='orange', font=('courier', 20, 'bold'),
                         relief='groove',
                         bd=10)
stop_button = tk.Button(buttons, text='STOP', command=stop, fg='yellow', bg='orange', font=('courier', 20, 'bold'),
                        relief='groove',
                        bd=10)

row1.pack()
row2.pack()
row3.pack(fill='x')

start_button.pack(side='left', fill='x', expand=True)
pause_button.pack(side='left', fill='x', expand=True)
stop_button.pack(side='right', fill='x', expand=True)
buttons.pack(fill='x')

lbl.pack(side="left", fill='x', expand=True)
lb.pack(side="left", fill='x', expand=True)
lbr.pack(side="right", fill='x', expand=True)
row4.pack(fill='x')

c.pack(fill='both', expand=True, padx=10, pady=10)
root.mainloop()
