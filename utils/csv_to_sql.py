import csv
import datetime
from dateutil.parser import parse
from value_maps import ethnicity, war_participated
from api.models import Client
from api.models import Services

def sync_client():
    with open('sample_data/client.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)
        ethnicity_funct = lambda k: [name for name in ethnicity.keys() if int(k[name])]
        war_participated_funct = lambda k: [war_participated[name] for name in war_participated.keys() if int(k[name])]
        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "uuid": row["UUID"],
                "first_name": row["First_Name"],
                "middle_name": row["Middle_Name"],
                "last_name": row["Last_Name"],
                "social_security": row["SSN"],
                "date_of_birth": fmt_date(row["DOB"]),
                "gender": int(row["Gender"]) if row['Gender'] else None,
                "veteran": int(row["VeteranStatus"]) if row['VeteranStatus'] else None,
                "year_entered": int(row["YearEnteredService"]) if row['YearEnteredService'] else None,
                "year_exited": int(row["YearSeparated"]) if row['YearSeparated'] else None,
                "military_branch": int(row["MilitaryBranch"]) if row['MilitaryBranch'] else None,
                "discharge_status": row["Discharge_Status"],
                "date_created": fmt_datetime(row["Date_Created"]),
                "date_updated": fmt_datetime(row["DateUpdated"]),
                "associate_id": row["UserID"],
                "ethnicity": ethnicity[ethnicity_funct(row)[0]],
                "war_participated": war_participated_funct(row)
            }

            bulk_create.append(Client(**csv2db_client))

def sync_disabilities():
    with open('sample_data/disabilities.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "":row["DisabilitiesID"],
                "":row["ProjectEntryID"],
                "":row["PersonalID"],
                "":row["InformationDate"],
                "":row["DisabilityType"],
                "":row["DisabilityResponse"],
                "":row["IndefiniteAndImpairs"],
                "":row["DocumentationOnFile"],
                "":row["ReceivingServices"],
                "":row["PATHHowConfirmed"],
                "":row["PATHSMIInformation"],
                "":row["TCellCountAvailable"],
                "":row["TCellCount"],
                "":row["TCellSource"],
                "":row["ViralLoadAvailable"],
                "":row["ViralLoad"],
                "":row["ViralLoadSource"],
                "":row["DataCollectionStage"],
                "":row["DateCreated"],
                "":row["DateUpdated"],
                "":row["UserID"],
                "":row["DateDeleted"],
                "":row["ExportID"]
            }
            bulk_create.append(Client(**csv2db_client))

def sync_employmenteducation():
    with open('sample_data/employmenteducation.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

                csv2db_client = {
                    "personal_id" : row["PersonalID"],
                    "project_entry_id" : row["ProjectEntryID"],
                    "services_id" : row["ServicesID"],
                    "date_provided" : fmt_date(row["DateProvided"]),
                    "record_type" : int(row["RecordType"]) if row['RecordType'] else None,
                    "type_provided" : int(row["TypeProvided"]) if row['TypeProvided'] else None,
                    "other_type_provided" : int(row["OtherTypeProvided"]) if row['OtherTypeProvided'] else None,
                    "sub_type_provided" = int(row["SubTypeProvided"]) if row['SubTypeProvided'] else None,
                    "fa_amount" : int(row["FAAmount"]) if row['FAAmount'] else None,
                    "referral_outcome" = row["ReferralOutcome"],
                    "date_created" : fmt_datetime(row["DateCreated"]),
                    "date_updated" : fmt_datetime(row["DateUpdated"]),
                    "associate_id" : row["UserID"]
                }

                bulk_create.append(Client(**csv2db_client))

            csv2db_client = {
                "":row["EmploymentEducationID"],
                "":row["ProjectEntryID"],
                "":row["PersonalID"],
                "":row["InformationDate"],
                "":row["LastGradeCompleted"],
                "":row["SchoolStatus"],
                "":row["Employed"],
                "":row["EmploymentType"],
                "":row["NotEmployedReason"],
                "":row["DataCollectionStage"],
                "":row["DateCreated"],
                "":row["DateUpdated"],
                "":row["UserID"],
                "":row["DateDeleted"]
            }
            bulk_create.append(Client(**csv2db_client))

def sync_enrollment():
    with open('sample_data/enrollment.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "project_entry_id": row["ProjectEntryID"],
                "personal_id": row["PersonalID"],
                "": row["ProjectID"],
                "entry_date": fmt_date(row["EntryDate"]),
                "household_id": row["HouseholdID"],
                "relationship_to_head_of_household": row["RelationshipToHoH"],
                "residence_prior": row["ResidencePrior"],
                "other_residence_prior": row["OtherResidencePrior"],
                "residence_prior_length_of_stay": row["ResidencePriorLengthOfStay"],
                "disabling_condition": row["DisablingCondition"],
                "entry_from_street_essh": row["EntryFromStreetESSH"],
                "date_to_street_essh": fmt_date(row["DateToStreetESSH"]),
                "times_homeless_past_three_years": row["TimesHomelessPastThreeYears"],
                "month_homeless_past_three_years": row["MonthsHomelessPastThreeYears"],
                "housing_status": row["HousingStatus"],
                "date_of_engagement": fmt_date(row["DateOfEngagement"]),
                "in_permanent_housing": row["InPermanentHousing"],
                "residential_move_in_date": fmt_date(row["ResidentialMoveInDate"]),
                "date_of_path_status": row["DateOfPATHStatus"],
                "client_enrolled_in_path": row["ClientEnrolledInPATH"],
                "reason_not_enrolled": row["ReasonNotEnrolled"],
                "worst_housing_situation": row["WorstHousingSituation"],
                "percent_ami": row["PercentAMI"],
                "last_permanent_street": row["LastPermanentStreet"],
                "last_permanent_city": row["LastPermanentCity"],
                "last_permanent_state": row["LastPermanentState"],
                "last_permanent_zip": row["LastPermanentZIP"],
                "": row["AddressDataQuality"],
                "date_of_bcp_status": row["DateOfBCPStatus"],
                "fysb_youth": row["FYSBYouth"],
                "reason_no_services": row["ReasonNoServices"],
                "sexual_orientation": row["SexualOrientation"],
                "formar_ward_child_welfare": row["FormerWardChildWelfare"],
                "": row["ChildWelfareYears"],
                "": row["ChildWelfareMonths"],
                "": row["FormerWardJuvenileJustice"],
                "juvenile_justice_years": row["JuvenileJusticeYears"],
                "juvenile_justice_months": row["JuvenileJusticeMonths"],
                "houshold_dynamics": row["HouseholdDynamics"],
                "sexual_orientation_gender_identity_youth": row["SexualOrientationGenderIDYouth"],
                "sexual_orientation_gender_identity_family": row["SexualOrientationGenderIDFam"],
                "housing_issues_youth": row["HousingIssuesYouth"],
                "housing_issues_family": row["HousingIssuesFam"],
                "school_or_educational_issues_youth": row["SchoolEducationalIssuesYouth"],
                "school_or_educational_issues_family": row["SchoolEducationalIssuesFam"],
                "unemployment_family": row["UnemploymentYouth"],
                "unemployment_family": row["UnemploymentFam"],
                "mental_health_issues_youth": row["MentalHealthIssuesYouth"],
                "mental_health_issues_family": row["MentalHealthIssuesFam"],
                "health_issues_youth": row["HealthIssuesYouth"],
                "health_issues_familty": row["HealthIssuesFam"],
                "physical_disability_youth": row["PhysicalDisabilityYouth"],
                "physical_disability_fam": row["PhysicalDisabilityFam"],
                "mental_disability_youth": row["MentalDisabilityYouth"],
                "mental_disability_fam": row["MentalDisabilityFam"],
                "abuse_and_neglect_youth": row["AbuseAndNeglectYouth"],
                "abuse_and_neglect_fam": row["AbuseAndNeglectFam"],
                "alcohol_drug_abuse_youth": row["AlcoholDrugAbuseYouth"],
                "alcohol_drug_abuse_fam": row["AlcoholDrugAbuseFam"],
                "insufficient_income": row["InsufficientIncome"],
                "active_military_parent": row["ActiveMilitaryParent"],
                "incarcerated_parent": row["IncarceratedParent"],
                "incarcerated_parent_status": row["IncarceratedParentStatus"],
                "referral_source": row["ReferralSource"],
                "": row["CountOutreachReferralApproaches"],
                "exchange_for_sex": row["ExchangeForSex"],
                "exchange_for_sex_past_three_months": row["ExchangeForSexPastThreeMonths"],
                "count_of_exchange_for_sex": row["CountOfExchangeForSex"],
                "asked_or_forced_to_exchange_for_sex": row["AskedOrForcedToExchangeForSex"],
                "": row["AskedOrForcedToExchangeForSexPastThreeMonths"],
                "work_place_violence_threats": row["WorkPlaceViolenceThreats"],
                "work_place_promise_difference": row["WorkplacePromiseDifference"],
                "coerced_to_continue_work": row["CoercedToContinueWork"],
                "labor_exploit_past_three_months": row["LaborExploitPastThreeMonths"],
                "hp_screening_score": row["HPScreeningScore"],
                "vamc_station": fmt_date(row["VAMCStation"]),
                "date_created": fmt_date(row["DateCreated"]),
                "date_updated": fmt_date(row["DateUpdated"]),
                "": row["UserID"],
                "": row["DateDeleted"]
            }
            bulk_create.append(Client(**csv2db_client))

def sync_exit():
    with open('sample_data/exit.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "ExitID"":row[""],
                "":row["ProjectEntryID"],
                "":row["PersonalID"],
                "":row["ExitDate"],
                "":row["Destination"],
                "":row["OtherDestination"],
                "":row["AssessmentDisposition"],
                "":row["OtherDisposition"],
                "":row["HousingAssessment"],
                "":row["SubsidyInformation"],
                "":row["ConnectionWithSOAR"],
                "":row["WrittenAftercarePlan"],
                "":row["AssistanceMainstreamBenefits"],
                "":row["PermanentHousingPlacement"],
                "":row["TemporaryShelterPlacement"],
                "":row["ExitCounseling"],
                "":row["FurtherFollowUpServices"],
                "":row["ScheduledFollowUpContacts"],
                "":row["ResourcePackage"],
                "":row["OtherAftercarePlanOrAction"],
                "":row["ProjectCompletionStatus"],
                "":row["EarlyExitReason"],
                "":row["FamilyReunificationAchieved"],
                "":row["DateCreated"],
                "":row["DateUpdated"],
                "":row["UserID"],
                "":row["DateDeleted"]
            }
            bulk_create.append()

def sync_funder():
    with open('sample_data/funder.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "":row["ExitID"],
                "":row["ProjectEntryID"],
                "":row["PersonalID"],
                "":row["ExitDate"],
                "":row["Destination"],
                "":row["OtherDestination"],
                "":row["AssessmentDisposition"],
                "":row["OtherDisposition"],
                "":row["HousingAssessment"],
                "":row["SubsidyInformation"],
                "":row["ConnectionWithSOAR"],
                "":row["WrittenAftercarePlan"],
                "":row["AssistanceMainstreamBenefits"],
                "":row["PermanentHousingPlacement"],
                "":row["TemporaryShelterPlacement"],
                "":row["ExitCounseling"],
                "":row["FurtherFollowUpServices"],
                "":row["ScheduledFollowUpContacts"],
                "":row["ResourcePackage"],
                "":row["OtherAftercarePlanOrAction"],
                "":row["ProjectCompletionStatus"],
                "":row["EarlyExitReason"],
                "":row["FamilyReunificationAchieved"],
                "":row["DateCreated"],
                "":row["DateUpdated"],
                "":row["UserID"],
                "":row["DateDeleted"]
            }
            bulk_create.append()

def sync_health_and_dv():
    with open('sample_data/healthanddv.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "":row["HealthAndDVID"],
                "":row["ProjectEntryID"],
                "":row["PersonalID"],
                "":row["InformationDate"],
                "":row["DomesticViolenceVictim"],
                "":row["WhenOccurred"],
                "":row["CurrentlyFleeing"],
                "":row["GeneralHealthStatus"],
                "":row["DentalHealthStatus"],
                "":row["MentalHealthStatus"],
                "":row["PregnancyStatus"],
                "":row["DueDate"],
                "":row["DataCollectionStage"],
                "":row["DateCreated"],
                "":row["DateUpdated"],
                "":row["UserID"],
                "":row["DateDeleted"]
            }
            bulk_create.append()



    import pdb; pdb.set_trace()
def sync_services():
    with open('sample_data/services.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create = []
        #Format functions where applicable
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)
        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

                csv2db_client = {
                    "personal_id" : row["PersonalID"],
                    "project_entry_id" : row["ProjectEntryID"],
                    "services_id" : row["ServicesID"],
                    "date_provided" : fmt_date(row["DateProvided"]),
                    "record_type" : int(row["RecordType"]) if row['RecordType'] else None,
                    "type_provided" : int(row["TypeProvided"]) if row['TypeProvided'] else None,
                    "other_type_provided" : int(row["OtherTypeProvided"]) if row['OtherTypeProvided'] else None,
                    "sub_type_provided" = int(row["SubTypeProvided"]) if row['SubTypeProvided'] else None,
                    "fa_amount" : int(row["FAAmount"]) if row['FAAmount'] else None,
                    "referral_outcome" = row["ReferralOutcome"],
                    "date_created" : fmt_datetime(row["DateCreated"]),
                    "date_updated" : fmt_datetime(row["DateUpdated"]),
                    "associate_id" : row["UserID"]
                }

                bulk_create.append(Client(**csv2db_client))
