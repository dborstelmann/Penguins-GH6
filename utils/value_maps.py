# -*- coding: utf-8 -*-

race = {
	1: "American Indian or Alaska Native",
	2: "Asian",
	3: "Black or African American",
	4: "Native Hawaiian or Other Pacific Islander",
	5: "White",
	6: "Hispanic/ Latino",
	8: "Client does not know",
	9: "Client refused",
	99: "Data not collected"
}

gender = {
	0: "Female",
	1: "Male",
	2: "Transgender male to female",
	3: "Transgender female to male",
	4: "Does not identify as male, female, or transgender",
	8: "Client does not know",
	9: "Client refused",
	99: "Data not collected"
}

general_boolean_numbers = {
	0: "No",
	1: "Yes",
	8: "Client does not know",
	9: "Client refused",
	99: "Data not collected"
}

general_status = {
	1: "Excellent",
	2: "Very Good",
	3: "Good",
	4: "Fair",
	5: "Poor",
	8: "Client does not know",
	9: "Client refused",
	99: "Data not collected"
}

employment_type = {
	1: "Full-time",
	2: "Part-time",
	3: "Seasonal / sporadic (including day labor)",
	99: "Data not Collected"
}

not_employed_reason = {
	1: "Looking For Work",
	2: "Unable to Work",
	3: "Not Looking for Work",
	99: "Data not Collected"
}

last_grade_completed = {
	1: "Less than Grade 5",
	2: "Grades 5-6",
	3: "Grades 7-8",
	4: "Grades 9-11",
	5: "Grade 12/ High School Diplomaa",
	6: "School Program does not have Grade Levels",
	7: "GED",
	10: "Some College",
	11: "Associates Degree",
	12: "Bachelors Degree",
	13: "Graduate Degree",
	14: "Vocational certification",
	8: "Client does not know",
	9: "Client refusted",
	99: "Data not collected"
}

when_experience_occured = {
	1: "Within past 3 months",
	2: "Three to Six Months Ago",
	3: "Six Months to One Year Ago",
	4: "One year ago or more",
	8: "Client does not know",
	9: "Client refused",
	99: "Data not collected"
}

POSSIBLE_AILMENTS = [
    "doctor",
    "sick",
    "medicine",
    "rehab",
    "hospital"
]

POSSIBLE_BENEFITS = [
    "case",
    "child",
    "care",
    "education",
    "school",
    "employment",
    "housing",
    "legal",
    "mentor",
    "support"
]

POSSIBLY_HOMELESS = [
    "homeless",
    "street",
    "evict",
    "out"
]

services_record_type = {
	12: "Contact",
	141: "Services Provided - PATH",
	142: "Services Provided - RHY",
	143: "Services Provided - HOPWA",
	144: "Services Provided - SSVF",
	151: "Financial Assistance - HOPWA",
	152: "Financial Assistance - SSVF",
	161: "Referrals Provided - PATH",
	162: "Referrals Provided - RHY",
	200: "Bed Night"
}

services_record_type_to_provided = {
	12: {
		1: "Place not meant for habitation",
		2: "Service setting, non-residential",
		3: "Service setting, residential"
	},
	141: {
		1: "Outreach",
		2: "Screening / assessment",
		3: "Habilitation / rehabilitation",
		4: "Community mental health",
		5: "Substance use treatment",
		6: "Case management",
		7: "Residential supportive services",
		8: "Housing minor renovation",
		9: "Housing moving assistance",
		10: "Housing technical assistance",
		11: "Security deposits",
		12: "One-time rent for eviction prevention",
		13: "Other PATH funded service"
	},
	142: {
		1: "Basic support services",
		2: "Community service / service learning (CSL)",
		3: "Counseling / therapy",
		4: "Dental care",
		5: "Education",
		6: "Employment and training services",
		7: "Criminal justice / legal services",
		8: "Life skills training",
		9: "Parenting education of parent of youth",
		10: "Parenting education for youth with children",
		11: "Peer (youth) counseling",
		12: "Post-natal care",
		13: "Pre-natal care",
		14: "Pre-natal care",
		15: "Psychological or psychiatric care",
		16: "Recreational activities",
		17: "Substance abuse assessment and/or treatment",
		18: "Substance abuse prevention",
		19: "Support group",
		20: "Preventative – overnight interim, respite",
		21: "Preventative – formal placement in an alternative setting outside of BCP",
		22: "Preventative – entry into BCP after preventative services",
		23: "Street outreach – health and hygiene products distributed",
		24: "Street outreach – food and drink items",
		25: "Street outreach – services information/brochures"
	},
	143: {
		1: "Adult day care and personal assistance",
		2: "Case management",
		3: "Child care",
		4: "Criminal justice/legal services",
		5: "Education",
		6: "Employment and training services",
		7: "Food/meals/nutritional services",
		8: "Health/medical care",
		9: "Life skills training",
		10: "Mental health care/counseling",
		11: "Outreach and/or engagement",
		12: "Substance abuse services/treatment",
		13: "Transportation",
		14: "Other HOPWA funded service"
	},
	144: {
		1: "Outreach services",
		2: "Case management service",
		3: "Assistance obtaining VA benefits",
		4: "Assistance obtaining / coordinating other public benefits",
		5: "Direct provision of other public benefits",
		6: "Other (non-TFA) supportive service approved by VA"
	},
	151: {
		1: "Rental Assistance",
		2: "Security Deposits",
		3: "Utility Deposits",
		4: "Utility Payments",
		7: "Mortgage Assistance"
	},
	152: {
		1: "Rental Assistance",
		2: "Security Deposits",
		3: "Utility Deposits",
		4: "Utility fee payments assistance",
		5: "Moving costs",
		8: "Transportation services: token / vouchers",
		9: "Transportation services: vehicle repair / maintenance",
		10: "Child Care",
		11: "General housing stability assistance - emergency supplies",
		12: "General housing stability assistance - other",
		14: "Emergency housing assistance"
	},
	161: {
		1: "Community mental health",
		2: "Substance use treatments",
		3: "Primary health services",
		4: "Job training",
		5: "Educational Services",
		6: "Relevant housing services",
		7: "Housing placement assistance",
		8: "Income assistance",
		9: "Employment assistance",
		10: "Medical assistance"
	},
	162: {
		1: "Child care non-TANF",
		2: "Supplemental nutritional assistance Program (food stamps)",
		3: "Education - liasion assistance to stay in school",
		4: "HUD Section 8 or permanent housing assistance",
		5: "Individual development account",
		6: "Medicaid"
	}
}
