import math


def entropy(data):
    yes = 0
    no = 0
    for row in data:
        if row[-1] == "Yes" or row[-1] == "+":
            yes += 1
        else:
            no += 1

    total = yes + no
    if yes == 0 or no == 0:
        return 0

    p1 = yes/total
    p2 = no/total

    return -(p1*math.log2(p1) + p2*math.log2(p2))


def information_gain(data, col):
    total_entropy = entropy(data)
    values = {}

    for row in data:
        key = row[col]
        if key not in values:
            values[key] = []
        values[key].append(row)

    sub_entropy = 0
    total = len(data)

    for key in values:
        prob = len(values[key]) / total
        sub_entropy += prob * entropy(values[key])

    return total_entropy - sub_entropy


def build_tree(data, attributes):

    classes = [row[-1] for row in data]

    if classes.count(classes[0]) == len(classes):
        return classes[0]

    if len(attributes) == 0:
        return max(set(classes), key=classes.count)

    gains = []
    for col in attributes:
        gains.append(information_gain(data, col))

    best = attributes[gains.index(max(gains))]

    tree = {best:{}}

    values = set([row[best] for row in data])

    for v in values:
        subset = [row for row in data if row[best] == v]

        if len(subset) == 0:
            tree[best][v] = max(set(classes), key=classes.count)
        else:
            new_attr = attributes.copy()
            new_attr.remove(best)
            tree[best][v] = build_tree(subset, new_attr)

    return tree


def print_tree(tree, names, level=0):

    if type(tree) != dict:
        print(":", tree)
        return

    for key in tree:
        for value in tree[key]:
            print("  "*level + names[key] + " =", value, end="")
            print_tree(tree[key][value], names, level+1)



# ---------------- Example 1 ----------------

data1 = [
["Sunny","Hot","High","Weak","No"],
["Sunny","Hot","High","Strong","No"],
["Overcast","Hot","High","Weak","Yes"],
["Rain","Mild","High","Weak","Yes"],
["Rain","Cool","Normal","Weak","Yes"],
["Rain","Cool","Normal","Strong","No"],
["Overcast","Cool","Normal","Strong","Yes"],
["Sunny","Mild","High","Weak","No"],
["Sunny","Cool","Normal","Weak","Yes"],
["Rain","Mild","Normal","Weak","Yes"],
["Sunny","Mild","Normal","Strong","Yes"],
["Overcast","Mild","High","Strong","Yes"],
["Overcast","Hot","Normal","Weak","Yes"],
["Rain","Mild","High","Strong","No"]
]

names1 = ["Outlook","Temp","Humidity","Wind"]

print("\nExample 1 Decision Tree\n")
tree1 = build_tree(data1,[0,1,2,3])
print_tree(tree1,names1)



# ---------------- Example 2 ----------------

data2 = [
["True","Hot","High","No"],
["True","Hot","High","No"],
["False","Hot","High","Yes"],
["False","Cool","Normal","Yes"],
["False","Cool","Normal","Yes"],
["True","Cool","High","No"],
["True","Hot","High","No"],
["True","Hot","Normal","Yes"],
["False","Cool","Normal","Yes"],
["False","Cool","High","Yes"]
]

names2 = ["A1","A2","A3"]

print("\n\nExample 2 Decision Tree\n")
tree2 = build_tree(data2,[0,1,2])
print_tree(tree2,names2)



# ---------------- Example 3 ----------------

data3 = [
["T","T","+"],
["T","T","+"],
["T","F","-"],
["F","F","+"],
["F","T","-"],
["F","T","-"]
]

names3 = ["A1","A2"]

print("\n\nExample 3 Decision Tree\n")
tree3 = build_tree(data3,[0,1])
print_tree(tree3,names3)
