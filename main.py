#!/usr/bin/env python3
"""
Equilibrium Statistic Calculator
A Python app that recursively calculates mean, median, and mode until convergence.
"""

import statistics
from collections import Counter
from typing import List, Tuple, Union
import matplotlib.pyplot as plt
import numpy as np


def calculate_mean(data: List[float]) -> float:
    """Calculate the arithmetic mean of a dataset."""
    return sum(data) / len(data)


def calculate_median(data: List[float]) -> float:
    """Calculate the median of a dataset."""
    return statistics.median(data)


def calculate_mode(data: List[float]) -> float:
    """
    Calculate the mode of a dataset.
    If multiple modes exist, return the smallest one.
    If no mode exists (all values unique), return the mean.
    """
    try:
        # Count frequencies
        counter = Counter(data)
        max_count = max(counter.values())

        # If all values appear once, no true mode exists
        if max_count == 1:
            return calculate_mean(data)

        # Find all modes (values with maximum frequency)
        modes = [value for value, count in counter.items() if count == max_count]

        # Return the smallest mode
        return min(modes)

    except Exception:
        # Fallback to mean if mode calculation fails
        return calculate_mean(data)


def check_stagnation(iteration_history: List[List[float]], stagnation_window: int = 1000) -> bool:
    """
    Check if the values have been identical for the last N iterations.
    Returns True if stagnated, False otherwise.
    """
    if len(iteration_history) < stagnation_window:
        return False

    # Get the last N iterations
    recent_iterations = iteration_history[-stagnation_window:]

    # Check if all iterations in the window are identical
    first_iteration = recent_iterations[0]
    for iteration in recent_iterations[1:]:
        if iteration != first_iteration:
            return False

    return True


def check_convergence(values: List[float], epsilon: float) -> bool:
    """
    Check if all values are within epsilon of each other.
    Returns True if converged, False otherwise.
    """
    if len(values) < 2:
        return True

    min_val = min(values)
    max_val = max(values)

    return (max_val - min_val) <= epsilon


def calculate_statistics(data: List[float]) -> Tuple[float, float, float]:
    """Calculate mean, median, and mode for a dataset."""
    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)

    return mean, median, mode


def format_values(values: List[float], precision: int = 6) -> str:
    """Format values for display with consistent precision."""
    return [round(v, precision) for v in values]


def equilibrium_statistic(initial_data: List[float], epsilon: Union[float, str] = 0.001, show_graph: bool = False) -> \
Tuple[float, List[List[float]]]:
    """
    Calculate the absolute statistic by recursively applying mean, median, mode
    until convergence within epsilon or stagnation.

    Args:
        initial_data: Initial dataset
        epsilon: Convergence threshold (float) or '*' for stagnation-only mode
        show_graph: Whether to return data for graphing

    Returns:
        Tuple of (converged_value, iteration_history) where iteration_history
        contains [mean, median, mode] for each iteration
    """

    stagnation_only = (epsilon == '*')

    print(f"🧮 Starting Equilibrium Statistic Calculation")
    print(f"📊 Initial Dataset: {format_values(initial_data)}")
    if stagnation_only:
        print(f"🎯 Mode: Stagnation-only (run until 1000 identical iterations)")
    else:
        print(f"🎯 Convergence Threshold (ε): {epsilon}")
    print("-" * 60)

    current_data = initial_data.copy()
    iteration = 0
    iteration_history = []

    while True:  # Run until convergence
        # Calculate statistics
        mean, median, mode = calculate_statistics(current_data)
        new_data = [mean, median, mode]

        # Store for graphing
        iteration_history.append([mean, median, mode])

        iteration += 1

        # Display current iteration
        print(f"Iteration {iteration}:")
        print(f"  Input:  {format_values(current_data)}")
        print(f"  Mean:   {round(mean, 6)}")
        print(f"  Median: {round(median, 6)}")
        print(f"  Mode:   {round(mode, 6)}")
        print(f"  Output: {format_values(new_data)}")

        # Check for convergence (only if not in stagnation-only mode)
        if not stagnation_only and check_convergence(new_data, epsilon):
            absolute_stat = sum(new_data) / len(new_data)  # Average of converged values
            print("-" * 60)
            print(f"✅ CONVERGENCE ACHIEVED after {iteration} iterations!")
            print(f"🎯 Absolute Statistic: {round(absolute_stat, 6)}")
            return absolute_stat, iteration_history

        # Check for stagnation (always check, but behavior depends on mode)
        if check_stagnation(iteration_history):
            absolute_stat = sum(new_data) / len(new_data)  # Average of stagnated values

            # Remove last 999 iterations from history for cleaner graphing
            if len(iteration_history) >= 1000:
                iteration_history = iteration_history[:-999]

            print("-" * 60)
            if stagnation_only:
                print(f"🔄 STAGNATION ACHIEVED after {iteration} iterations!")
                print(f"   Values have been identical for the last 1000 iterations.")
            else:
                print(f"🔄 STAGNATION DETECTED after {iteration} iterations!")
                print(f"   Values have been identical for the last 1000 iterations.")
            print(f"🎯 Absolute Statistic: {round(absolute_stat, 6)}")
            return absolute_stat, iteration_history

        # Show progress info
        if stagnation_only:
            print(f"  Status: Running until stagnation...")
        else:
            spread = max(new_data) - min(new_data)
            print(f"  Spread: {round(spread, 6)} (target: ≤ {epsilon})")
        print()

        # Update data for next iteration
        current_data = new_data


def plot_convergence(iteration_history: List[List[float]], epsilon: Union[float, str], final_value: float):
    """
    Plot the convergence of mean, median, and mode over iterations.

    Args:
        iteration_history: List of [mean, median, mode] for each iteration
        epsilon: Convergence threshold (float) or '*' for stagnation-only mode
        final_value: Final converged value
    """
    if not iteration_history:
        print("❌ No data to plot.")
        return

    stagnation_only = (epsilon == '*')

    # Convert to arrays for easier plotting
    iterations = range(1, len(iteration_history) + 1)
    means = [stats[0] for stats in iteration_history]
    medians = [stats[1] for stats in iteration_history]
    modes = [stats[2] for stats in iteration_history]

    # Create the plot
    plt.figure(figsize=(12, 8))

    # Plot the three statistics
    plt.plot(iterations, means, 'b-o', label='Mean', linewidth=2, markersize=6)
    plt.plot(iterations, medians, 'r-s', label='Median', linewidth=2, markersize=6)
    plt.plot(iterations, modes, 'g-^', label='Mode', linewidth=2, markersize=6)

    # Add convergence zone (only if not in stagnation-only mode)
    if len(iteration_history) > 1 and not stagnation_only:
        plt.axhline(y=final_value + epsilon / 2, color='orange', linestyle='--', alpha=0.7, label=f'±ε/2 zone')
        plt.axhline(y=final_value - epsilon / 2, color='orange', linestyle='--', alpha=0.7)
        plt.fill_between(iterations, final_value - epsilon / 2, final_value + epsilon / 2,
                         color='yellow', alpha=0.2, label='Convergence Zone')

    # Add final convergence line
    plt.axhline(y=final_value, color='black', linestyle='-', linewidth=2, alpha=0.8,
                label=f'Absolute Statistic: {final_value:.6f}')

    # Styling
    plt.xlabel('Iteration', fontsize=12, fontweight='bold')
    plt.ylabel('Value', fontsize=12, fontweight='bold')

    if stagnation_only:
        plt.title('Equilibrium Statistic Convergence (Stagnation Mode)', fontsize=16, fontweight='bold')
    else:
        plt.title('Equilibrium Statistic Convergence', fontsize=16, fontweight='bold')

    plt.grid(True, alpha=0.3)
    plt.legend(loc='best', frameon=True, fancybox=True, shadow=True)

    # Set reasonable axis limits
    all_values = means + medians + modes
    y_min, y_max = min(all_values), max(all_values)
    y_range = y_max - y_min
    if y_range > 0:
        plt.ylim(y_min - 0.1 * y_range, y_max + 0.1 * y_range)

    plt.tight_layout()

    # Show plot
    plt.show()

    # Print summary statistics
    print("\n📈 Convergence Analysis:")
    print(f"   • Total iterations: {len(iteration_history)}")
    print(f"   • Initial spread: {max(iteration_history[0]) - min(iteration_history[0]):.6f}")
    print(f"   • Final spread: {max(iteration_history[-1]) - min(iteration_history[-1]):.6f}")
    print(
        f"   • Convergence rate: {((max(iteration_history[0]) - min(iteration_history[0])) / max(1e-10, max(iteration_history[-1]) - min(iteration_history[-1]))):.2f}x reduction")


def get_user_input() -> Tuple[List[float], Union[float, str], bool]:
    """Get dataset, epsilon (or '*' for stagnation-only), and graph preference from user input."""

    print("🧑‍💻 Equilibrium Statistic Calculator")
    print("=" * 50)

    # Get dataset
    while True:
        try:
            data_input = input("📥 Enter numbers separated by commas: ").strip()
            data = [float(x.strip()) for x in data_input.split(',') if x.strip()]

            if len(data) < 1:
                print("❌ Please enter at least one number.")
                continue

            break

        except ValueError:
            print("❌ Invalid input. Please enter numbers separated by commas.")

    # Get epsilon
    while True:
        try:
            epsilon_input = input("🎯 Enter convergence threshold (default 0.001, '*' for stagnation-only): ").strip()

            if not epsilon_input:
                epsilon = 0.001
            elif epsilon_input == '*':
                epsilon = '*'  # Special flag for stagnation-only mode
            else:
                epsilon = float(epsilon_input)

                if epsilon <= 0:
                    print("❌ Epsilon must be positive.")
                    continue

            break

        except ValueError:
            print("❌ Invalid epsilon. Please enter a positive number or '*' for stagnation-only mode.")

    # Get graph preference
    while True:
        graph_input = input("📊 Do you want to see a convergence graph? (Y/n): ").strip().lower()

        if graph_input in ['', 'y', 'yes', '1', 'true']:  # Default to yes (empty input = yes)
            show_graph = True
            break
        elif graph_input in ['n', 'no', '0', 'false']:
            show_graph = False
            break
        else:
            print("❌ Please enter 'y' for yes or 'n' for no (default is yes).")

    return data, epsilon, show_graph


def main():
    """Main application entry point."""
    try:
        # Get user input
        data, epsilon, show_graph = get_user_input()

        print("\n" + "=" * 60)

        # Calculate absolute statistic
        result, history = equilibrium_statistic(data, epsilon, show_graph=show_graph)

        print("=" * 60)
        print(f"🏆 FINAL RESULT: The Absolute Statistic is {round(result, 6)}")

        # Show graph if requested
        if show_graph:
            print("\n🎨 Generating convergence graph...")
            try:
                plot_convergence(history, epsilon, result)
            except Exception as e:
                print(f"❌ Could not generate graph: {e}")
                print("💡 Make sure matplotlib is installed: pip install matplotlib")

    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")


if __name__ == "__main__":
    main()