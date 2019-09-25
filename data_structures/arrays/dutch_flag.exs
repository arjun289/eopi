defmodule DutchNationalFlag do
  @moduledoc """
  A sample of Dutch National flag problem.

  Module should have function to generate random
  list of balls of color red, white, blue.

  It should expose function to solve the problem and
  return the result in dutch flag format.
  """

  defp ball(:red), do: 1
  defp ball(:white), do: 2
  defp ball(:blue), do: 3

  @balls ~w(red white blue)a

  defp random_ball, do: Enum.random(@balls)
  defp random_ball(n), do: (for _ <- 1..n, do: random_ball())

  defp is_dutch([]), do: true
  defp is_dutch([_]), do: true
  defp is_dutch([b, h|l]), do: ball(b) < ball(h) and is_dutch([h|l])
  defp is_dutch(_), do: false

  defp dutch(list), do: dutch([], [], [], list)
  defp dutch(r, w, b, []), do: r ++ w ++ b
  defp dutch(r, w, b, [:red | list]), do: dutch([:red | r], w, b, list)
  defp dutch(r, w, b, [:white | list]), do: dutch(r, [:white | w], b, list)
  defp dutch(r, w, b, [:blue | list]), do: dutch(r, w, [:blue | b], list)

  def dutch_national_flag(n) do
    list = random_ball(n)
    if is_dutch(list) do
      IO.puts("The list => #{inspect(list)} is already in dutch flag format!" )
    else
      result = dutch(list)
      IO.puts("The initial list is: #{inspect(list)}")
      IO.puts("The resultant list after solving is: #{inspect(result)}")
    end
  end
end

DutchNationalFlag.dutch_national_flag(10)
