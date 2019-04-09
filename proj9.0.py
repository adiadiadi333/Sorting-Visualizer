import tkinter as tk
import time


def delay(t):
    global root, zero
    now = time.time()
    while time.time() - now < t / 1000:
        root.update()
        lbr.config(text="Time: %f" % (time.time() - zero))
        lbl.config(text='Swaps: %d, Comparisons: %d' % (steps, cmps))


# SORTING ALGORITHMS

# BUBBLE SORT
def bubsort(l):
    global cmps
    for i in range(len(l) - 1):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                cmps += 1
                delay(slider2.get())
                l[j], l[j + 1] = l[j + 1], l[j]
                yield l


# INSERTION SORT
def insort(l):
    global cmps
    for i in range(1, len(l)):
        curval = l[i]
        pos = i
        cmps += 1
        delay(slider2.get())
        while pos > 0 and l[pos - 1] > curval:
            cmps += 2
            delay(slider2.get() * 2)
            l[pos] = l[pos - 1]
            pos -= 1
            yield l
        l[pos] = curval
        yield l


# SELECTION SORT
def selsort(l):
    global cmps
    for i in range(len(l) - 1):
        min_idx = i
        for j in range(i + 1, len(l)):
            if l[min_idx] > l[j]:
                cmps += 1
                delay(slider2.get())
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]
        yield l


# MERGE SORT
def merge_sort(arr):
    global cmps
    n = len(arr) - 1
    count = 1
    begin = 0
    end = 0
    cmps += 1
    delay(slider2.get())
    while count <= n:
        cmps += 2
        delay(slider2.get() * 2)
        while end < n:
            cmps += 1
            delay(slider2.get())
            mid = begin + count // 2
            end = begin + count
            if (begin < n) and (end <= n):
                cmps += 2
                delay(slider2.get() * 2)
                yield from merge(arr, begin, mid, end)
                begin = end + 1
            else:
                yield from merge(arr, begin - count - 1, begin - 1, n)
        count = 2 * count + 1
        begin = 0
        end = 0


# Merge Function
def merge(a, l, m, r):
    global cmps
    n1 = m - l + 1
    n2 = r - m
    left = [0] * n1
    right = [0] * n2
    for i in range(0, n1):
        left[i] = a[l + i]
    for i in range(0, n2):
        right[i] = a[m + i + 1]
    i, j, kay = 0, 0, l
    cmps += 2
    delay(slider2.get() * 2)
    while i < n1 and j < n2:
        cmps += 2
        delay(slider2.get() * 2)
        if left[i] > right[j]:
            a[kay] = right[j]
            j += 1
        else:
            a[kay] = left[i]
            i += 1
        kay += 1
        yield a
    cmps += 1
    delay(slider2.get())
    while i < n1:
        cmps += 1
        delay(slider2.get())
        a[kay] = left[i]
        i += 1
        kay += 1
        yield a
    cmps += 1
    delay(slider2.get())
    while j < n2:
        cmps += 1
        delay(slider2.get())
        a[kay] = right[j]
        j += 1
        kay += 1
        yield a


# HEAP SORT
def heap_sort(l):
    global cmps
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
                cmps += 2
                delay(slider2.get() * 2)
            if index < i and l[j] < l[index]:
                cmps += 2
                delay(slider2.get() * 2)
                l[j], l[index] = l[index], l[j]
                yield l
            j = index
            if index >= i:
                cmps += 1
                delay(slider2.get())
                break


# Build Heap
def buildMaxHeap(l, n):
    global cmps
    for i in range(n):
        if l[i] > l[int((i - 1) / 2)]:
            cmps += 2
            delay(slider2.get() * 2)
            j = i
            while l[j] > l[int((j - 1) / 2)]:
                cmps += 1
                delay(slider2.get())
                (l[j],
                 l[int((j - 1) / 2)]) = (l[int((j - 1) / 2)],
                                         l[j])
                j = int((j - 1) / 2)
                yield l


# QUICK SORT

def quick_sort(array, lo, hi):
    global cmps
    if lo < hi:
        cmps += 1
        delay(slider2.get())

        pivot_index = hi
        pivot_value = array[pivot_index]
        store_index = lo
        for i in range(lo, hi):
            if array[i] <= pivot_value:
                cmps += 1
                delay(slider2.get())
                if i != store_index:
                    array[i], array[store_index] = array[store_index], array[i]
                    yield array
                store_index += 1

        if pivot_index != store_index:
            array[pivot_index], array[store_index] = array[store_index], array[pivot_index]
            yield array

        yield from quick_sort(array, lo, store_index - 1)
        yield from quick_sort(array, store_index + 1, hi)


sort_dic = {
    "bubble": bubsort,
    "insertion": insort,
    "selection": selsort,
    "merge": merge_sort,
    "heap": heap_sort,
    "quick": lambda l: quick_sort(l, 0, len(l) - 1)
}

sorts = ["bubble", "insertion", "selection", "merge", "heap", "quick"]

# GUI
root = tk.Tk()
root.config(bg='#9400d3')
root.title('Sorting Visualizer')
root.geometry('700x700+400+50')

row1 = tk.Frame(root, bg='red', bd=5, relief='groove')

tk.Label(row1, text='SIZE OF ARRAY:', fg='yellow', bg='green', font=('courier', 20, 'bold')).pack(side="left")
e = tk.Scale(row1, from_=1, to=1000, orient='horizontal', fg='white', bg='green', font=('courier', 20, 'bold'),
             troughcolor='red', activebackground='orange', highlightbackground='red')
e.set(100)
e.pack(side="right", fill='x', expand=True)

row2 = tk.Frame(root, bg='red', bd=5, relief='groove')

tk.Label(row2, text='SORTING ALGORITHM:', font=('courier', 20, 'bold'), fg='yellow', bg='green').pack(side="left",
                                                                                                      fill='x',
                                                                                                      expand=True)
choice = tk.StringVar(row2)
menu = tk.OptionMenu(row2, choice, *sorts)
menu.config(fg='white', bg='green', font=('courier', 20, 'bold'), highlightbackground='orange',
            activebackground='yellow')
choice.set("selection")
menu.pack(side="right", fill='x', expand=True)

row2p5 = tk.Frame(root, bg='red', bd=5, relief='groove')

tk.Label(row2p5, text='TIME PER COMPARISON(ms):', fg='yellow', bg='green', font=('courier', 20, 'bold')).pack(
    side="left")
slider2 = tk.Scale(row2p5, from_=0, to=1000, orient='horizontal', fg='white', bg='green', font=('courier', 20, 'bold'),
                   troughcolor='orange', activebackground='yellow', highlightbackground='orange')
slider2.set(100)
slider2.pack(side="right", fill='x', expand=True)

row3 = tk.Frame(root, bg='red', bd=5, relief='groove')

tk.Label(row3, text='TIME PER SWAP(ms):', fg='yellow', bg='green', font=('courier', 20, 'bold')).pack(
    side="left")
slider = tk.Scale(row3, from_=1, to=1000, orient='horizontal', fg='white', bg='green', font=('courier', 20, 'bold'),
                  troughcolor='orange', activebackground='yellow', highlightbackground='orange')
slider.set(100)
slider.pack(side="right", fill='x', expand=True)

row4 = tk.Frame(root, bd=5, relief='sunken')
lbl = tk.Label(row4, text='Swaps: %d, Comparisons: %d' % (0, 0), fg='light blue', font=('courier', 20, 'italic'), bd=5,
               bg='#c776b9',
               relief='raised')
lb = tk.Label(row4, text='START', fg='light blue', font=('courier', 20, 'italic'), bd=5, bg='#c776b9', relief='raised')
lbr = tk.Label(row4, text='Time: %f' % 0, fg='light blue', font=('courier', 20, 'italic'), bd=5, bg='#c776b9',
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
zero = 0
steps = 0
cmps = 0


def start():
    global c, stopped, paused, zero, steps, cmps

    stopped = False
    paused = False

    steps = 0
    cmps = 0
    zero = time.time() + 2
    pause_zero = 0.0

    root.update()
    c.delete("all")
    lb.config(text="this is the array")
    lbl.config(text='Swaps: %d, Comparisons: %d' % (steps, cmps))
    lbr.config(text="Time: %d" % 0.0)
    n = int(e.get())

    sl = [i for i in range(n, 0, -1)]

    visualize(sl)
    delay(2000)
    lb.config(text="sorting")

    zero = time.time()

    g = sort_dic[choice.get()]

    for l_iter in g(sl):
        c.delete("all")
        visualize(l_iter)
        steps += 1
        lbl.config(text='Swaps: %d, Comparisons: %d' % (steps, cmps))
        now = time.time()
        while time.time() - now < slider.get() / 1000:
            root.update()
            lbr.config(text="Time: %f" % (time.time() - zero))
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

row1.pack(fill='x')
row2.pack(fill='x')
row2p5.pack(fill='x')
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
