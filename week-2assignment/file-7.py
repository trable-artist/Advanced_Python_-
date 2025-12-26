items = input().split()
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1

print("Purchase frequency:")
for item, count in counts.items():
    print(f"{item}: {count}")

most_popular = ""
max_count = 0
for item, count in counts.items():
    if count > max_count:
        max_count = count
        most_popular = item
print(f"\nMost popular item: {most_popular}")

once = []
for item, count in counts.items():
    if count == 1:
        once.append(item)
print(f"Purchased once: {' '.join(once)}")

sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
print("\nSorted by frequency:")
for item, count in sorted_items:
    print(f"{item} {count}")
