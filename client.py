class AiDevopsWorkspaceCanaryReleaseGateClient:
    def evaluate_canary_deployment(self, service_name='auth-gateway', canary_weight_pct=10):
        metrics = [
            {'metric': 'P99 Latency', 'baseline_ms': 120, 'canary_ms': 118, 'verdict': 'HEALTHY'},
            {'metric': 'Error Rate (5xx)', 'baseline_pct': 0.02, 'canary_pct': 0.01, 'verdict': 'HEALTHY'},
            {'metric': 'CPU Utilization', 'baseline_pct': 44.0, 'canary_pct': 42.5, 'verdict': 'HEALTHY'}
        ]
        return {
            'service_name': service_name,
            'canary_weight_pct': canary_weight_pct,
            'metrics_comparison': metrics,
            'gate_decision': 'PROMOTE_CANARY_TO_100_PERCENT',
            'rollback_triggered': False,
            'release_confidence_pct': 99.2
        }
