ELASTICSEARCH_URL="http://localhost:9200"
curl -X PUT "${ELASTICSEARCH_URL}/copilot_usage_total" -H 'Content-Type: application/json' -d @mapping/copilot_usage_total_mapping.json
curl -X PUT "${ELASTICSEARCH_URL}/copilot_usage_breakdown" -H 'Content-Type: application/json' -d @mapping/copilot_usage_breakdown_mapping.json
curl -X PUT "${ELASTICSEARCH_URL}/copilot_usage_breakdown_chat" -H 'Content-Type: application/json' -d @mapping/copilot_usage_breakdown_chat_mapping.json
curl -X PUT "${ELASTICSEARCH_URL}/copilot_seat_info_settings" -H 'Content-Type: application/json' -d @mapping/copilot_seat_info_settings_mapping.json
curl -X PUT "${ELASTICSEARCH_URL}/copilot_seat_assignments" -H 'Content-Type: application/json' -d @mapping/copilot_seat_assignments_mapping.json
