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
                "":row["ProjectEntryID"],
                "":row["PersonalID"],
                "":row["ProjectID"],
                "":row["EntryDate"],
                "":row["HouseholdID"],
                "":row["RelationshipToHoH"],
                "":row["ResidencePrior"],
                "":row["OtherResidencePrior"],
                "":row["ResidencePriorLengthOfStay"],
                "":row["DisablingCondition"],
                "":row["EntryFromStreetESSH"],
                "":row["DateToStreetESSH"],
                "":row["TimesHomelessPastThreeYears"],
                "":row["MonthsHomelessPastThreeYears"],
                "":row["HousingStatus"],
                "":row["DateOfEngagement"],
                "":row["InPermanentHousing"],
                "":row["ResidentialMoveInDate"],
                "":row["DateOfPATHStatus"],
                "":row["ClientEnrolledInPATH"],
                "":row["ReasonNotEnrolled"],
                "":row["WorstHousingSituation"],
                "":row["PercentAMI"],
                "":row["LastPermanentStreet"],
                "":row["LastPermanentCity"],
                "":row["LastPermanentState"],
                "":row["LastPermanentZIP"],
                "":row["AddressDataQuality"],
                "":row["DateOfBCPStatus"],
                "":row["FYSBYouth"],
                "":row["ReasonNoServices"],
                "":row["SexualOrientation"],
                "":row["FormerWardChildWelfare"],
                "":row["ChildWelfareYears"],
                "":row["ChildWelfareMonths"],
                "":row["FormerWardJuvenileJustice"],
                "":row["JuvenileJusticeYears"],
                "":row["JuvenileJusticeMonths"],
                "":row["HouseholdDynamics"],
                "":row["SexualOrientationGenderIDYouth"],
                "":row["SexualOrientationGenderIDFam"],
                "":row["HousingIssuesYouth"],
                "":row["HousingIssuesFam"],
                "":row["SchoolEducationalIssuesYouth"],
                "":row["SchoolEducationalIssuesFam"],
                "":row["UnemploymentYouth"],
                "":row["UnemploymentFam"],
                "":row["MentalHealthIssuesYouth"],
                "":row["MentalHealthIssuesFam"],
                "":row["HealthIssuesYouth"],
                "":row["HealthIssuesFam"],
                "":row["PhysicalDisabilityYouth"],
                "":row["PhysicalDisabilityFam"],
                "":row["MentalDisabilityYouth"],
                "":row["MentalDisabilityFam"],
                "":row["AbuseAndNeglectYouth"],
                "":row["AbuseAndNeglectFam"],
                "":row["AlcoholDrugAbuseYouth"],
                "":row["AlcoholDrugAbuseFam"],
                "":row["InsufficientIncome"],
                "":row["ActiveMilitaryParent"],
                "":row["IncarceratedParent"],
                "":row["IncarceratedParentStatus"],
                "":row["ReferralSource"],
                "":row["CountOutreachReferralApproaches"],
                "":row["ExchangeForSex"],
                "":row["ExchangeForSexPastThreeMonths"],
                "":row["CountOfExchangeForSex"],
                "":row["AskedOrForcedToExchangeForSex"],
                "":row["AskedOrForcedToExchangeForSexPastThreeMonths"],
                "":row["WorkPlaceViolenceThreats"],
                "":row["WorkplacePromiseDifference"],
                "":row["CoercedToContinueWork"],
                "":row["LaborExploitPastThreeMonths"],
                "":row["HPScreeningScore"],
                "":row["VAMCStation"],
                "":row["DateCreated"],
                "":row["DateUpdated"],
                "":row["UserID"],
                "":row["DateDeleted"]
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
