import math

# --- CLI User Inputs ---
print("--- CONCRETE MIX DESIGN: NEWTON-RAPHSON METHOD ---")
A = float(input("Enter constant A (e.g., 96): "))
B = float(input("Enter constant B (e.g., 7): "))
fc = float(input("Enter target compressive strength fc in MPa (e.g., 30): "))
tolerance = float(input("Enter tolerance (e.g., 0.00001): "))
print("-" * 85)

def f(x):
    return (A / (B ** x)) - fc

def df(x):
    return -A * math.log(B) / (B ** x)

x_n = 0.6
iter_n = 0
results = []

while True:
    f_xn = f(x_n)
    df_xn = df(x_n)

    results.append(f"Iter {iter_n:<2} | w/c: {x_n:.4f} | f(x): {f_xn:>8.4f}")

    if abs(f_xn) < tolerance or df_xn == 0:
        break

    x_next = x_n - (f_xn / df_xn)

    if abs(x_next - x_n) < tolerance:
        x_n = x_next
        results.append(f"Iter {iter_n + 1:<2} | w/c: {x_n:.4f} | f(x): {f(x_n):>8.4f}")
        break

    x_n = x_next
    iter_n += 1

# Loop through and print two columns per row
for i in range(0, len(results), 2):
    print("   ||   ".join(results[i:i + 2]))

print("-" * 85)
print(f"Final optimal w/c: {x_n:.4f}")