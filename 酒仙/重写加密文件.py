# f = function (x, y) {
# #         var a = 0, b = 0, c = 0;
# #         x = x.split("");
# #         y = y || 99;
# #         while ((a = x.shift()) && (b = a.charCodeAt(0) - 77.5)) c = (Math.abs(b) < 13 ? (b + 48.5) : parseInt(a, 36)) + y * c;
# #         return c
# #     }
def parseint(string):
    return int(''.join([x for x in string if x.isdigit()]))
def f(x,y):
    a = 0
    b = 0
    c = 0
    x = x.split(" ")
    if y:
        pass
    else:
        y=99
    del x[0]
    while True:
        a = x.pop(0)
        b = ord(a[0]) - 77.5
        if a and b:
            if abs(b)<13:
                c = int('dfg',base=36)
            elif abs(b)< b + 48.5:
                c = y * c
            return c

f('sdcsac',6)