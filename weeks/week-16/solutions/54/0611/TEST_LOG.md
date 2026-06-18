# TEST_LOG

## Stage 1 — test_timing（綠燈）

```
test_edge_case_exception_still_records ... ok
test_edge_case_multiple_calls_accumulates ... ok
test_edge_case_no_params_and_none_return ... ok
test_preserves_function_metadata ... ok
test_records_elapsed_time ... ok
test_returns_original_result ... ok
----------------------------------------------------------------------
Ran 6 tests in 0.000s
OK
```

## Stage 2 — test_sorts（綠燈）

```
test_all_equal ... ok
test_already_sorted ... ok
test_basic_cases ... ok
test_input_not_mutated ... ok
test_random_data_matches_builtin ... ok
test_reverse_sorted ... ok
test_uncomparable_elements ... ok
----------------------------------------------------------------------
Ran 7 tests in 0.003s
OK
```

## Stage 3 — test_sorts（含加速版，綠燈）

```
test_all_equal ... ok
test_already_sorted ... ok
test_basic_cases ... ok
test_input_not_mutated ... ok
test_random_data_matches_builtin ... ok
test_reverse_sorted ... ok
test_uncomparable_elements ... ok
----------------------------------------------------------------------
Ran 7 tests in 0.003s
OK
```

## Stage 4 — test_plot（綠燈）

```
test_load_results_keys_are_ints ... ok
test_load_results_returns_dict ... ok
test_plot_output_png_exists ... ok
----------------------------------------------------------------------
Ran 3 tests in 0.172s
OK
```

## Stage 5 — test_security（綠燈）

```
test_load_results_rejects_non_dict_json ... ok
test_make_data_rejects_negative_n ... ok
test_sorts_no_unused_random_import ... ok
----------------------------------------------------------------------
Ran 3 tests in 0.002s
OK
```

## 全部測試（最終綠燈）

```
test_load_results_keys_are_ints ... ok
test_load_results_returns_dict ... ok
test_plot_output_png_exists ... ok
test_load_results_rejects_non_dict_json ... ok
test_make_data_rejects_negative_n ... ok
test_sorts_no_unused_random_import ... ok
test_all_equal ... ok
test_already_sorted ... ok
test_basic_cases ... ok
test_input_not_mutated ... ok
test_random_data_matches_builtin ... ok
test_reverse_sorted ... ok
test_uncomparable_elements ... ok
test_edge_case_exception_still_records ... ok
test_edge_case_multiple_calls_accumulates ... ok
test_edge_case_no_params_and_none_return ... ok
test_preserves_function_metadata ... ok
test_records_elapsed_time ... ok
test_returns_original_result ... ok
----------------------------------------------------------------------
Ran 19 tests in 0.181s
OK
```
