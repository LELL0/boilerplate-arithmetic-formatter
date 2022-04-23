def arithmetic_arranger(problems, solutionFlag=False):
    numOfProblems = len(problems)
    r = 3
    solutions = []
    arranged_problems = ''

    for i in range(len(problems)):
        if type(problems[i]) == type([]):
            problems = [j for sub in problems for j in sub]
            numOfProblems = len(problems)

    if numOfProblems > 5:
        return "Error: Too many problems."
    counter = 0
    for problem in problems:
        solutions.append([0, 0, 0, 0])
        problem = problem.split(' ')

        if not problem[1] == '+' and not problem[1] == '-':
            return "Error: Operator must be '+' or '-'."
        elif not problem[0].isnumeric() or not problem[2].isnumeric():
            return "Error: Numbers must only contain digits."
        elif len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            # calculating the number of ' ' and number of '-'
            if(len(problem[0]) > len(problem[2])):
                solutions[counter][2] = (len(problem[0])+2) * '-'
            else:
                solutions[counter][2] = (len(problem[2])+2) * '-'

            solutions[counter][0] = ' ' * \
                (len(solutions[counter][2])-len(problem[0])) + problem[0]
            solutions[counter][1] = problem[1]+' ' * \
                (len(solutions[counter][2])-len(problem[2])-1) + problem[2]

            if (solutionFlag):
                r = 4
                if problem[1] == '+':
                    sol = int(problem[0]) + int(problem[2])
                    solutions[counter][3] = (
                        len(solutions[counter][2]) - len(str(sol))) * ' ' + str(sol)

                elif problem[1] == '-':
                    sol = int(problem[0]) - int(problem[2])
                    solutions[counter][3] = (
                        len(solutions[counter][2]) - len(str(sol))) * ' ' + str(sol)
        counter += 1

    for i in range(r):
        for j in range(numOfProblems):
            if(j == numOfProblems-1):
                arranged_problems += str(solutions[j][i])
            else:
                arranged_problems += str(solutions[j][i])+'    '
        if not i == r-1:
            arranged_problems += '\n'

    return arranged_problems
