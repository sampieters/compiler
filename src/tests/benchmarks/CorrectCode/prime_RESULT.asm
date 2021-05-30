.data
string1_1: .asciiz "Enter the number of prime numbers required\n\00"
string2_1: .asciiz ""
string2_2: .asciiz "\00"
string3_1: .asciiz "First "
string3_2: .asciiz " prime numbers are :\n\00"
string4_1: .asciiz "2\n\00"
string5_1: .asciiz ""
string5_2: .asciiz "\n\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -28
        sw      $fp, 28($sp)
        move    $fp, $sp
        li      $8, 3
        sw      $8, 8($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $8, 4($fp)
        addiu   $8, $fp, 4
        la      $4, string2_1
        li      $v0, 4
        syscall 
        sw      $8, 24($fp)
        lw      $4, 24($fp)
        li      $v0, 5
        syscall 
        sw      $v0, 4($fp)
        la      $4, string2_2
        li      $v0, 4
        syscall 
        # BEGIN IF CONDITION
        lw      $8, 4($fp)
        sge     $8, $8, 1
        beq     $8,$0, $L0
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string3_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string3_2
        li      $v0, 4
        syscall 
        la      $4, string4_1
        li      $v0, 4
        syscall 
        # END IF BODY
$L0:    
        li      $8, 2
        sw      $8, 12($fp)
                
$L1:    
        # BEGIN WHILE CONDITION
        lw      $8, 12($fp)
        lw      $9, 4($fp)
        sle     $8, $8, $9
        beq     $8, $0, $L6
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        li      $8, 2
        sw      $8, 16($fp)
                
$L2:    
        # BEGIN WHILE CONDITION
        lw      $8, 8($fp)
        subi    $8, $8, 1
        lw      $8, 16($fp)
        sle     $8, $8, $8
        beq     $8, $0, $L4
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        # BEGIN IF CONDITION
        lw      $8, 8($fp)
        lw      $9, 16($fp)
        NIET ZOMAAR$8, $8, $9
        seq     $8, $8, 0
        beq     $8,$0, $L3
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        j       $L4
        # END IF BODY
$L3:    
        lw      $8, 16($fp)
        addiu   $8, $8, 1
        sw      $8, 16($fp)
        j       $L2
        # END WHILE BODY
                
$L4:    
        # BEGIN IF CONDITION
        lw      $8, 16($fp)
        lw      $9, 8($fp)
        seq     $8, $8, $9
        beq     $8,$0, $L5
        nop     
        # END IF CONDITION
                
        # BEGIN IF BODY
        la      $4, string5_1
        li      $v0, 4
        syscall 
        lw      $4, 8($fp)
        li      $v0, 1
        syscall 
        la      $4, string5_2
        li      $v0, 4
        syscall 
        lw      $8, 12($fp)
        addiu   $8, $8, 1
        sw      $8, 12($fp)
        # END IF BODY
$L5:    
        lw      $8, 8($fp)
        addiu   $8, $8, 1
        sw      $8, 8($fp)
        j       $L1
        # END WHILE BODY
                
$L6:    
        nop     
        move    $sp, $fp
        lw      $fp, 28($sp)
        addiu   $sp, $sp, 32
        li      $v0, 10
        syscall 