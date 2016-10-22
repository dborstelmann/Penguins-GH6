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

def sync_income_benefits():
    with open('sample_data/income_benefits') as csvfile:
        reader = csv.DictReader(csvfile)
        bulk_create = []

        fmt_date = lambda k: parse(k).date()
        fmt_datetime = lambda k: parse(k)
        cast_int = lambda k: int(k) if k else None
        cast_bool = lambda k : bool(k) if k else None
        for row in reader:
            for key in row:
                if row[key] == 'NULL':
                    row[key] = None

            csv2db_client = {
                "income_benefits_id":row["IncomeBenefitsID"],
                "project_entry_id":row["ProjectEntryID"],
                "personal_id":row["PersonalID"],
                "information_date":fmt_date(row["InformationDate"],)
                "income_from_any_source":cast_int(row["IncomeFromAnySource"]),
                "total_monthly_income":cast_int(row["TotalMonthlyIncome"]),
                "earned":cast_bool(row["Earned"]),
                "earned_amount":cast_int(row["EarnedAmount"]),
                "unemployment":cast_bool(row["Unemployment"]),
                "unemployment_amount":cast_int(row["UnemploymentAmount"]),
                "ssi":cast_bool(row["SSI"]),
                "ssi_amount":cast_int(row["SSIAmount"]),
                "ssdi":cast_bool(row["SSDI"]),
                "ssdi_amont":cast_bool(row["SSDIAmount"]),
                "va_disability_service":cast_bool(row["VADisabilityService"]),
                "va_disability_service_amount":cast_int(row["VADisabilityServiceAmount"]),
                "va_disability_non_service":cast_bool(row["VADisabilityNonService"]),
                "va_disability_non_service_amount":cast_int(row["VADisabilityNonServiceAmount"]),
                "private_disability":cast_bool(row["PrivateDisability"]),
                "private_disability_amount":cast_int(row["PrivateDisabilityAmount"]),
                "workers_comp":cast_bool(row["WorkersComp"]),
                "workers_comp_amount":cast_int(row["WorkersCompAmount"]),
                "tanf":cast_bool(row["TANF"]),
                "tanf_amount":cast_int(row["TANFAmount"]),
                "ga":cast_bool(row["GA"]),
                "ga_amount":cast_int(row["GAAmount"]),
                "soc_sec_retirement":cast_bool(row["SocSecRetirement"]),
                "soc_sec_retirement_amount":cast_int(row["SocSecRetirementAmount"]),
                "pension":cast_bool(row["Pension"]),
                "pension_amount":cast_int(row["PensionAmount"]),
                "child_support":cast_bool(row["ChildSupport"]),
                "child_support_amount":cast_int(row["ChildSupportAmount"]),
                "alimony":cast_bool(row["Alimony"])
                "alimony_amount":cast_int(row["AlimonyAmount"])
                "other_income_source":cast_bool(row["OtherIncomeSource"]),
                "other_income_source_amount":cast_int(row["OtherIncomeAmount"]),
                "other_income_source_identify":row["OtherIncomeSourceIdentify"],
                "benefits_from_any_source":cast_bool(row["BenefitsFromAnySource"]),
                "snap":cast_bool(row["SNAP"]),
                "wic":cast_bool(row["WIC"]),
                "tanf_child_care":cast_bool(row["TANFChildCare"]),
                "tanf_transportation":cast_bool(row["TANFTransportation"]),
                "other_tanf":cast_bool(row["OtherTANF"]),
                "rental_assistance_ongoing":cast_bool(row["RentalAssistanceOngoing"]),
                "rental_assistance_temp":cast_bool(row["RentalAssistanceTemp"]),
                "other_benefits_source":cast_bool(row["OtherBenefitsSource"]),
                "other_benefits_source_identify":row["OtherBenefitsSourceIdentify"],
                "insurance_from_any_source":cast_bool(row["InsuranceFromAnySource"]),
                "medicaid":cast_bool(row["Medicaid"]),
                "no_medicaid_reason":cast_int(row["NoMedicaidReason"]),
                "medicare":cast_bool(row["Medicare"])
                "no_medicare_reason":cast_int(row["NoMedicareReason"]),
                "schip":cast_bool(row["SCHIP"]),
                "no_schip_reason":row["NoSCHIPReason"],
                "va_medical_services":cast_bool(row["VAMedicalServices"]),
                "no_va_med_reason":row["NoVAMedReason"],
                "employer_provided":cast_bool(row["EmployerProvided"]),
                "no_employer_provided_reason":row["NoEmployerProvidedReason"],
                "cobra":cast_bool(row["COBRA"]),
                "no_cobra_reason":row["NoCOBRAReason"],
                "private_pay":cast_bool(row["PrivatePay"]),
                "no_private_pay_reason":row["NoPrivatePayReason"],
                "state_health_ins":row["StateHealthIns"],
                "no_state_health_ins_reason":row["NoStateHealthInsReason"],
                "hiv_aids_assistance":cast_bool(row["HIVAIDSAssistance"]),
                "no_hiv_aids_assistance_reason":row["NoHIVAIDSAssistanceReason"],
                "adap":cast_bool(row["ADAP"]),
                "no_adap_reason":row["NoADAPReason"],
                "data_collection_stage":cast_int(row["DataCollectionStage"]),
                "date_created":fmt_datetime(row["DateCreated"]),
                "date_updated":fmt_datetime(row["DateUpdated"]),
                "associate_id":row["UserID"]
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
