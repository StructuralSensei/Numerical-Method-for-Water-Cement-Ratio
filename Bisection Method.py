# --- CLI User Inputs ---
print("--- CONCRETE MIX DESIGN: BISECTION METHOD ---")
A = float(input("Enter constant A (e.g., 96): "))
B = float(input("Enter constant B (e.g., 7): "))
fc = float(input("Enter target compressive strength fc in MPa (e.g., 30): "))
tolerance = float(input("Enter tolerance (e.g., 0.00001): "))
print("-" * 85)


def f(x):
    return (A / (B ** x)) - fc


x_low, x_high = 0.4, 0.8
iter_b = 0

# NEW: Create an empty list to store our rows of data instead of printing immediately
results = []

while (x_high - x_low) / 2.0 > tolerance:
    x_n = (x_low + x_high) / 2.0
    f_xn = f(x_n)

    # NEW: Format the text and 'append' (add) it to our results list.
    # The >8 ensures the numbers right-align neatly.
    results.append(f"Iter {iter_b:<2} | w/c: {x_n:.4f} | f(x): {f_xn:>8.4f}")

    if f(x_low) * f_xn < 0:
        x_high = x_n
    else:
        x_low = x_n

    iter_b += 1

# NEW: Loop through our list, jumping 2 steps at a time.
for i in range(0, len(results), 2):
    # Grab two items at once and join them with a double-line separator ( || )
    print("   ||   ".join(results[i:i + 2]))

print("-" * 85)
print(f"Final optimal w/c: {x_n:.4f}")