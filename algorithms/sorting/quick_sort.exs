defmodule Quicksort do
  @doc """
  Naive quicksort implementation of quick sort with
  worst case performance of O(n^2).
  """
  def quicksort_naive([]), do: []
  def quicksort_naive([pivot|t]) do
    quicksort_naive(for x <- t, x < pivot, do: x)
    ++ [pivot] ++
    quicksort_naive(for x <- t, x >= pivot, do: x)
  end

  @doc """
  Quick sort algorithm with pivot chosen randomly.
  """
  def quicksort_random([]), do: []
  def quicksort_random(list) do
    list
    |> List.pop_at(random_position(list))
    |> _quicksort_random()
  end

  defp _quicksort_random({nil, _}), do: []
  defp _quicksort_random({pivot, []}), do: [pivot]
  defp _quicksort_random({pivot, sublist}) do
    smaller_sublist = for item <- sublist, item < pivot, do: item
    larger_sublist = for item <- sublist, item >= pivot, do: item

    _quicksort_random(List.pop_at(smaller_sublist, random_position(smaller_sublist)))
    ++ [pivot]
    ++ _quicksort_random(List.pop_at(larger_sublist, random_position(larger_sublist)))
  end

  defp random_position([]), do: 0
  defp random_position(list), do: :rand.uniform(length(list)) - 1


  @doc """
  Quick sort algorithm with the pivot chosen as median of 3
  numbers.
  """

  def quicksort_median([]), do: []
  def quicksort_median(list) do
    list
    |> List.pop_at(list_median(list))
    |> _quicksort_median()
  end

  defp _quicksort_median({nil, _}), do: []
  defp _quicksort_median({pivot, []}), do: [pivot]
  defp _quicksort_median({pivot, sublist}) do
    smaller_sublist = for item <- sublist, item < pivot, do: item
    larger_sublist = for item <- sublist, item >= pivot, do: item

    _quicksort_median(List.pop_at(smaller_sublist, list_median(smaller_sublist)))
    ++ [pivot]
    ++ _quicksort_median(List.pop_at(larger_sublist, list_median(larger_sublist)))
  end

  defp list_median(list) when length(list) < 3, do: 0
  defp list_median(list) do
    median =
      list
      |> Enum.take_random(3)
      |> case do
        [a, b, c] when (a >= b and a <= c) or (a <= b and a >= c) -> a
        [a, b, c] when (b >= a and b <= c) or (b <= a and b >= c) -> b
        [_, _, c] -> c
      end
    Enum.find_index(list, fn x -> x == median end)
  end
end

[10,4,6,2,3,8]
|> Quicksort.quicksort_median()
|> IO.inspect()
