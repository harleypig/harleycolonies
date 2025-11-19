# Chat & Control

This document contains all settings related to chat & control.

## Settings

### `censorCoordinates`

**Type**: `Boolean`  
**Default**: `false`  

Censor coordinates in goals and block positions

---

### `censorRanCommands`

**Type**: `Boolean`  
**Default**: `false`  

Censor arguments to ran commands, to hide, for example, coordinates to #goal

---

### `chatControl`

**Type**: `Boolean`  
**Default**: `true`  

Allow chat based control of Baritone. Most likely should be disabled when Baritone is imported for use in something else

---

### `chatControlAnyway`

**Type**: `Boolean`  
**Default**: `false`  

Some clients like Impact try to force chatControl to off, so here's a second setting to do it anyway

---

### `chatDebug`

**Type**: `Boolean`  
**Default**: `false`  

Print all the debug messages to chat

---

### `desktopNotifications`

**Type**: `Boolean`  
**Default**: `false`  

Desktop notifications

---

### `echoCommands`

**Type**: `Boolean`  
**Default**: `true`  

Echo commands to chat when they are run

---

### `elytraChatSpam`

**Type**: `Boolean`  
**Default**: `false`  

Verbose chat logging in elytra mode

---

### `logAsToast`

**Type**: `Boolean`  
**Default**: `false`  

Shows popup message in the upper right corner, similarly to when you make an advancement

---

### `prefix`

**Type**: `String`  
**Default**: `"#"`  

The command prefix for chat control

---

### `prefixControl`

**Type**: `Boolean`  
**Default**: `true`  

Whether or not to allow you to run Baritone commands with the prefix

---

### `shortBaritonePrefix`

**Type**: `Boolean`  
**Default**: `false`  

Use a short Baritone prefix [B] instead of [Baritone] when logging to chat

---

### `toastTimer`

**Type**: `Long`  
**Default**: `5000`  

The time of how long the message in the pop-up will display

If below 1000L (1sec), it's better to disable this

---

### `verboseCommandExceptions`

**Type**: `Boolean`  
**Default**: `false`  

Print out ALL command exceptions as a stack trace to stdout, even simple syntax errors

---


[← Back to Settings Index](baritone/SETTINGS)
