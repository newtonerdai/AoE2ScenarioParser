# Changelog

All changes made to the scenario file will be documented in this file.

---

## Scenario v1.41

### Added

-   Map:
    -   Between `script_name` and `collide_and_correct`
        ```json
        "block_humanity_team_change": {
            "type": "u8",
            "default": 0
        },
        ```

## Scenario v1.40

### Added

-   DataHeader.PlayerDataOneStruct:

    -   Between `civilization` and `cty_mode`
        ```json
        "architecture_set": {
          "type": "u32",
          "default": 36
        },
        ```

-   Map:

    -   Between `map_color_mood` and `collide_and_correct`
        ```json
        "separator_3": {
            "type": "2",
            "default": "600a"
        },
        "script_name": {
            "type": "str16",
            "default": "",
            "dependencies": {
                "on_commit": {
                    "action": "REFRESH",
                    "target": "Files:script_file_path"
                }
            }
        },
        ```
    -   Between `villager_force_drop` and `player_1_camera_y`
        ```json
        "unknown": {
            "type": "128",
            "default": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
        },
        ```

-   Triggers.trigger.condition:

    -   After: `target_player`
        ```json
        "unit_ai_action": {
            "type": "s32",
            "default": -1
        },
        "unknown_4": {
            "type": "s32",
            "default": -1
        },
        "xs_function": {
            "type": "str32",
            "default": ""
        }
        ```

-   Triggers.trigger.effect:

    -   Between: `play_sound` and `message`
        ```json
        "player_color": {
            "type": "s32",
            "default": -1
        },
        "unknown_4": {
            "type": "s32",
            "default": -1
        },
        ```

-   Files:

```json
      "Files": {
        "retrievers": {
            "unknown_2": {
                "type": "4",
                "default": "00000000"
            },
            "script_file_path": {
                "type": "str16",
                "default": null,
                "dependencies": {
                    "on_refresh": {
                        "action": "SET_VALUE",
                        "target": "Map:script_name",
                        "eval": "script_name + ('.xs' if len(script_name) > 0 else '')"
                    }
                }
            },
            "script_file_content": {
                "type": "str32",
                "default": ""
            },
            "ai_files_present": {
                "type": "u32",
                "default": 0,
                "dependencies": {
                    "on_refresh": {
                        "action": "SET_VALUE",
                        "target": "self:number_of_ai_files",
                        "eval": "0 if number_of_ai_files == 0 else 1"
                    }
                }
            },
            "unknown_4": {
                "type": "4",
                "default": "00000000"
            },
            "number_of_ai_files": {
                "type": "u32",
                "default": [],
                "potential_list": false,
                "dependencies": {
                    "on_construct": {
                        "action": "SET_REPEAT",
                        "target": "self:ai_files_present"
                    },
                    "on_refresh": [
                        {
                            "action": "SET_VALUE",
                            "target": "self:ai_files",
                            "eval": "len(ai_files)"
                        },
                        {
                            "action": "SET_REPEAT",
                            "target": "self:ai_files",
                            "eval": "1 if len(ai_files) > 0 else 0"
                        }
                    ],
                    "on_commit": {
                        "action": "REFRESH",
                        "target": "self:ai_files_present"
                    }
                }
            },
            "ai_files": {
                "type": "struct:AI2Struct",
                "default": [],
                "dependencies": {
                    "on_refresh": {
                        "action": "SET_REPEAT",
                        "target": "self:number_of_ai_files",
                        "eval": "number_of_ai_files if number_of_ai_files != [] else 0"
                    },
                    "on_construct": {
                        "action": "REFRESH_SELF"
                    },
                    "on_commit": {
                        "action": "REFRESH",
                        "target": "self:number_of_ai_files"
                    }
                }
            },
            "__END_OF_FILE_MARK__": {
                "type": "1",
                "comment": "Should always be last retriever",
                "default": ""
            }
        },
        "structs": {
            "AI2Struct": {
                "retrievers": {
                    "ai_file_name": {
                        "type": "str32",
                        "default": ""
                    },
                    "ai_file": {
                        "type": "str32",
                        "default": ""
                    }
                }
            }
        }
    }
```

### Removed

-   FileHeader:

    -   Between `scenario_instructions` and `player_count`
        ```json
        "individual_victories_used": {
          "type": "u32",
          "default": 0
        },
        ```
