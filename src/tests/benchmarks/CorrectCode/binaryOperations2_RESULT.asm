.data
string1_1: .asciiz ""
string1_2: .asciiz "; \00"
string2_1: .asciiz ""
string2_2: .asciiz "; \00"
string3_1: .asciiz ""
string3_2: .asciiz "; \00"
string4_1: .asciiz ""
string4_2: .asciiz "; \00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -12
        sw      $fp, 8($sp)
        sw      $ra, 4($sp)
        sw      $4, 0($sp)
        move    $fp, $sp
        la      $4, string1_1
        li      $2, 4
        syscall 
        li      $4, 10
        li      $2, 1
        syscall 
        la      $4, string1_2
        li      $2, 4
        syscall 
        la      $4, string2_1
        li      $2, 4
        syscall 
        li      $4, 10
        li      $2, 1
        syscall 
        la      $4, string2_2
        li      $2, 4
        syscall 
        la      $4, string3_1
        li      $2, 4
        syscall 
        li      $4, 10
        li      $2, 1
        syscall 
        la      $4, string3_2
        li      $2, 4
        syscall 
        la      $4, string4_1
        li      $2, 4
        syscall 
        li      $4, 10
        li      $2, 1
        syscall 
        la      $4, string4_2
        li      $2, 4
        syscall 
        li      $v0, 1
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 0($sp)
        lw      $ra, 4($sp)
        lw      $fp, 8($sp)
        addiu   $sp, $sp, 12
        li      $2, 10
        syscall 