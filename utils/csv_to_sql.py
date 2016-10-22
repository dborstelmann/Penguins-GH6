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
        cast_int = lambda k: int(k) if k else None

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "disabilities_id":row["DisabilitiesID"],
                "project_entry_id":row["ProjectEntryID"],
                "personal_id":row["PersonalID"],
                "information_date":fmt_date(row["InformationDate"]),
                "disability_type":cast_int(row["DisabilityType"]),
                "indefinite_and_impairs":cast_int(row["IndefiniteAndImpairs"]),
                "documentation_on_file":cast_int(row["DocumentationOnFile"]),
                "receiving_services":cast_int(row["ReceivingServices"]),
                "path_how_confirmed":cast_int(row["PATHHowConfirmed"]),
                "data_collection_stage":cast_int(row["DataCollectionStage"]),
                "date_created":fmt_datetime(row["DateCreated"]),
                "date_updated":fmt_datetime(row["DateUpdated"]),
                "associate_id":row["UserID"],
            }
            bulk_create.append(Client(**csv2db_client))

def sync_employmenteducation():
    with open('sample_data/employmenteducation.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)
        cast_int = lambda k: int(k) if k else None

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "employment_education_id":row["EmploymentEducationID"],
                "project_entry_id":row["ProjectEntryID"],
                "personal_id":row["PersonalID"],
                "information_date":fmt_date(row["InformationDate"]),
                "last_grade_completed": cast_int(row["LastGradeCompleted"]),
                "school_status":cast_int(row["SchoolStatus"]),
                "employed":cast_int(row["Employed"]),
                "employment_type": cast_int(row["EmploymentType"]),
                "not_employed_reason": cast_int(row["NotEmployedReason"]),
                "data_collection_stage": cast_int(row["DataCollectionStage"]),
                "date_created": fmt_datetime(row["DateCreated"]),
                "date_updated": fmt_datetime(row["DateUpdated"]),
                "associate_id": row["UserID"],
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
        cast_int = lambda k: int(k) if k else None

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "exit_id":row["ExitID"],
                "project_entry_id":row["ProjectEntryID"],
                "personal_id":row["PersonalID"],
                "exit_date":fmt_date(row["ExitDate"]),
                "destination":cast_int(row["Destination"]),
                "other_destination":cast_int(row["OtherDestination"]),
                "assessment_disposition":cast_int(row["AssessmentDisposition"]),
                "other_disposition":cast_int(row["OtherDisposition"]),
                "housing_assessment":cast_int(row["HousingAssessment"]),
                "subsidy_information":cast_int(row["SubsidyInformation"]),
                "connection_with_soar":cast_int(row["ConnectionWithSOAR"]),
                "written_after_care_plan":cast_int(row["WrittenAftercarePlan"]),
                "assistance_mainstream_benefits":cast_int(row["AssistanceMainstreamBenefits"]),
                "permanent_housing_placement":cast_int(row["PermanentHousingPlacement"]),
                "temporary_shelter_placement":cast_int(row["TemporaryShelterPlacement"]),
                "exit_counseling":cast_int(row["ExitCounseling"]),
                "further_follow_up_services":cast_int(row["FurtherFollowUpServices"]),
                "scheduled_follow_up_contact":cast_int(row["ScheduledFollowUpContacts"]),
                "resource_package":cast_int(row["ResourcePackage"]),
                "other_aftercare_plan_or_action":cast_int(row["OtherAftercarePlanOrAction"]),
                "project_completion_status":cast_int(row["ProjectCompletionStatus"]),
                "early_exit_reason":cast_int(row["EarlyExitReason"]),
                "family_reunification_achieved":cast_int(row["FamilyReunificationAchieved"]),
                "date_created":fmt_datetime(row["DateCreated"]),
                "date_updated":fmt_datetime(row["DateUpdated"]),
                "associate_id":row["UserID"]
            }
            bulk_create.append()

def sync_health_and_dv():
    with open('sample_data/healthanddv.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create  = []
        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)
        cast_int = lambda k: int(k) if k else None

        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "health_and_dv_id":row["HealthAndDVID"],
                "project_entry_id":row["ProjectEntryID"],
                "personal_id":row["PersonalID"],
                "information_date":fmt_date(row["InformationDate"]),
                "domestic_violence_victim":cast_int(row["DomesticViolenceVictim"]),
                "when_occured":cast_int(row["WhenOccurred"]),
                "currently_fleeing":cast_int(row["CurrentlyFleeing"]),
                "general_health_status":cast_int(row["GeneralHealthStatus"]),
                "dental_health_status":cast_int(row["DentalHealthStatus"]),
                "mental_health_status":cast_int(row["MentalHealthStatus"]),
                "pregnancy_status":cast_int(row["PregnancyStatus"]),
                "due_date":fmt_date(row["DueDate"]),
                "date_collection_stage":row["DataCollectionStage"],
                "date_created":fmt_datetime(row["DateCreated"]),
                "date_updated":fmt_datetime(row["DateUpdated"]),
                "associate_id":row["UserID"]
            }
            bulk_create.append()

def income_benefits():
    with open('sample_data/income_benefits') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create = []

        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)
        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "":row["IncomeBenefitsID"]
                "":row["ProjectEntryID"]
                "":row["PersonalID"]
                "":row["InformationDate"]
                "":row["IncomeFromAnySource"]
                "":row["TotalMonthlyIncome"]
                "":row["Earned"]
                "":row["EarnedAmount"]
                "":row["Unemployment"]
                "":row["UnemploymentAmount"]
                "":row["SSI"]
                "":row["SSIAmount"]
                "":row["SSDI"]
                "":row["SSDIAmount"]
                "":row["VADisabilityService"]
                "":row["VADisabilityServiceAmount"]
                "":row["VADisabilityNonService"]
                "":row["VADisabilityNonServiceAmount"]
                "":row["PrivateDisability"]
                "":row["PrivateDisabilityAmount"]
                "":row["WorkersComp"]
                "":row["WorkersCompAmount"]
                "":row["TANF"]
                "":row["TANFAmount"]
                "":row["GA"]
                "":row["GAAmount"]
                "":row["SocSecRetirement"]
                "":row["SocSecRetirementAmount"]
                "":row["Pension"]
                "":row["PensionAmount"]
                "":row["ChildSupport"]
                "":row["ChildSupportAmount"]
                "":row["Alimony"]
                "":row["AlimonyAmount"]
                "":row["OtherIncomeSource"]
                "":row["OtherIncomeAmount"]
                "":row["OtherIncomeSourceIdentify"]
                "":row["BenefitsFromAnySource"]
                "":row["SNAP"]
                "":row["WIC"]
                "":row["TANFChildCare"]
                "":row["TANFTransportation"]
                "":row["OtherTANF"]
                "":row["RentalAssistanceOngoing"]
                "":row["RentalAssistanceTemp"]
                "":row["OtherBenefitsSource"]
                "":row["OtherBenefitsSourceIdentify"]
                "":row["InsuranceFromAnySource"]
                "":row["Medicaid"]
                "":row["NoMedicaidReason"]
                "":row["Medicare"]
                "":row["NoMedicareReason"]
                "":row["SCHIP"]
                "":row["NoSCHIPReason"]
                "":row["VAMedicalServices"]
                "":row["NoVAMedReason"]
                "":row["EmployerProvided"]
                "":row["NoEmployerProvidedReason"]
                "":row["COBRA"]
                "":row["NoCOBRAReason"]
                "":row["PrivatePay"]
                "":row["NoPrivatePayReason"]
                "":row["StateHealthIns"]
                "":row["NoStateHealthInsReason"]
                "":row["HIVAIDSAssistance"]
                "":row["NoHIVAIDSAssistanceReason"]
                "":row["ADAP"]
                "":row["NoADAPReason"]
                "":row["DataCollectionStage"]
                "":row["DateCreated"]
                "":row["DateUpdated"]
                "":row["UserID"]
            }

            bulk_create.append(Client(**csv2db_client))


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
