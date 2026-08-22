from client import AiDevopsWorkspaceCanaryReleaseGateClient

def main():
    client = AiDevopsWorkspaceCanaryReleaseGateClient()
    res = client.evaluate_canary_deployment('billing-engine', 15)
    print('Service: ' + res['service_name'] + ' (' + str(res['canary_weight_pct']) + '% traffic) | Decision: ' + res['gate_decision'])
    print('Confidence: ' + str(res['release_confidence_pct']) + '% | Rollback: ' + str(res['rollback_triggered']))
    for m in res['metrics_comparison']:
        print('  [' + m['verdict'] + '] ' + m['metric'] + ' (Baseline: ' + str(m['baseline_ms'] if 'baseline_ms' in m else m.get('baseline_pct')) + ' vs Canary: ' + str(m.get('canary_ms', m.get('canary_pct'))) + ')')

if __name__ == '__main__':
    main()
