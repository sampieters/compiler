.data
string1_1: .asciiz ""
string1_2: .asciiz "; \00"
string2_1: .asciiz ""
string2_2: .asciiz "; \00"
string3_1: .asciiz ""
string3_2: .asciiz "; \00"
string4_1: .asciiz ""
string4_2: .asciiz "; \00"
string5_1: .asciiz ""
string5_2: .asciiz "; \00"
string6_1: .asciiz ""
string6_2: .asciiz "; \00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -32
        sw      $fp, 28($sp)
        sw      $ra, 24($sp)
        sw      $4, 20($sp)
        move    $fp, $sp
        li      $8, 9
        sw      $8, 0($fp)
        la      $4, string1_1
        li      $2, 4
        syscall 
        li      $4, 9
        li      $2, 1
        syscall 
        la      $4, string1_2
        li      $2, 4
        syscall 
        lw      $8, 0($fp)
        addiu   $8, $8, 1
        sw      $8, 0($fp)
        la      $4, string2_1
        li      $2, 4
        syscall 
        lw      $4, 0($fp)
        li      $2, 1
        syscall 
        la      $4, string2_2
        li      $2, 4
        syscall 
        li      $9, 15
        sw      $9, 4($fp)
        li      $10, 12
        sw      $10, 8($fp)
        li      $10, 12
        sw      $10, 0($fp)
        lw      $12, 8($fp)
        subi    $12, $12, 1
        sw      $12, 12($fp)
        lw      $12, 12($fp)
        sw      $12, 8($fp)
        la      $4, string3_1
        li      $2, 4
        syscall 
        lw      $4, 8($fp)
        li      $2, 1
        syscall 
        la      $4, string3_2
        li      $2, 4
        syscall 
        la      $4, string4_1
        li      $2, 4
        syscall 
        lw      $4, 0($fp)
        li      $2, 1
        syscall 
        la      $4, string4_2
        li      $2, 4
        syscall 
        lw      $13, 0($fp)
        addiu   $13, $13, 1
        sw      $13, 0($fp)
        la      $4, string5_1
        li      $2, 4
        syscall 
        lw      $4, 0($fp)
        li      $2, 1
        syscall 
        la      $4, string5_2
        li      $2, 4
        syscall 
        lw      $15, 4($fp)
        subi    $15, $15, 1
        sw      $15, 16($fp)
        lw      $15, 16($fp)
        sw      $15, 4($fp)
        la      $4, string6_1
        li      $2, 4
        syscall 
        lw      $4, 4($fp)
        li      $2, 1
        syscall 
        la      $4, string6_2
        li      $2, 4
        syscall 
        li      $v0, 1
        j       $FUNC_main
$FUNC_main:
        move    $sp, $fp
        lw      $4, 20($sp)
        lw      $ra, 24($sp)
        lw      $fp, 28($sp)
        addiu   $sp, $sp, 32
        li      $2, 10
        syscall 