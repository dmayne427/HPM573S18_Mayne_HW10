import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov


# simulating mono therapy
# create a cohort
cohort_mono = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.MONO)
# simulate the cohort
simOutputs_mono = cohort_mono.simulate()

# simulating combination therapy
# create a cohort
cohort_combo = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.COMBO)
# simulate the cohort
simOutputs_combo = cohort_combo.simulate()

# draw survival curves and histograms
SupportMarkov.draw_survival_curves_and_histograms(simOutputs_mono, simOutputs_combo)

# print the estimates for the mean survival time and mean time to AIDS
SupportMarkov.print_outcomes(simOutputs_mono, "No Anticoagulation Therapy:")
SupportMarkov.print_outcomes(simOutputs_combo, "Anticoagulation Therapy:")

# print comparative outcomes
SupportMarkov.print_comparative_outcomes(simOutputs_mono, simOutputs_combo)

# report the CEA results
SupportMarkov.report_CEA_CBA(simOutputs_mono, simOutputs_combo)

print('I would recommend adopting this anticoagulation drug at a willingness-to-pay of approximately $6,000 or greater, to ensure a positive net monetary benefit')
