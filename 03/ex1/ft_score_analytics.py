import sys

if __name__ == "__main__":
    args = sys.argv
    if len(args) <= 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        scores = [0] * (len(args) - 1)
        i = 0
        try:
            while i < len(args) - 1:
                scores[i] = int(args[i + 1])
                i = i + 1
            print("Scores processed: [", end="")
            i = 0
            while i < len(scores):
                print(scores[i], end="")
                if not i == len(scores) - 1:
                    print(", ", end="")
                i = i + 1
            print("]")
            print("Total players:", len(scores))
            print("Total score:", sum(scores))
            print("Average score:", sum(scores) / len(scores))
            print("High score:", max(scores))
            print("Low score:", min(scores))
            print("Score range", max(scores) - min(scores))
        except ValueError:
            print("Invalid input, only numbers are accepted")
