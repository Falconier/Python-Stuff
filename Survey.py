'''
Survey.py: store and analyze survey result
'''

def main():
    raw_data = getSurveyData()
    individuals = surveyPerPerson(raw_data)
    print(raw_data)
    print(individuals)

    print(surveryPerQuestion(raw_data))


#get survey data
def getSurveyData():
	survey_data = {}
	survey_data["p1"] = [5,4,4,5,3,5]
	survey_data["p2"] = [5,5,3,5,4,3]
	survey_data["p3"] = [3,4,5,4,3,5]
	survey_data["p4"] = [4,5,4,5,3,5]
	survey_data["p5"] = [2,3,4,3,5,4]

	return survey_data

def surveyPerPerson(data):
	data = dict(data)
	individuals_data = {}
	for p in data:
		total = 0
		for score in data[p]:
			total += score
		individuals_data[p] = total / len(data[p])
	return individuals_data

#returns a dictionary that contains each question's average score
def surveryPerQuestion(data):
    allVals = list(data.values())
    for i in range(0,len(allVals)):
        indVals = list(allVals[i])
        for j in range(0,len(indVals)):
            print(allVals[i][j])
        # print(allVals[i])
    print(allVals[0][0])
    return allVals


#returns a dictionary that contains count for each rating
def surveyOverall(data):
    pass

main()
