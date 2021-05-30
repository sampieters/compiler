.data
string1_1: .asciiz ""
string1_2: .asciiz ";\00"
.globl main
.text
                
main:   
        addiu   $sp, $sp, -8
        sw      $fp, 8($sp)
        move    $fp, $sp
        li      $8, 0
        sw      $8, 4($fp)
                
$L0:    
        # BEGIN WHILE CONDITION
        lw      $8, 4($fp)
        slti    $8, $8, 5
        beq     $8, $0, $L1
        nop     
        # END WHILE CONDITION
                
        # BEGIN WHILE BODY
        lw      $8, 4($fp)
        addiu   $8, $8, 1
        sw      $8, 4($fp)
        la      $4, string1_1
        li      $v0, 4
        syscall 
        lw      $4, 4($fp)
        li      $v0, 1
        syscall 
        la      $4, string1_2
        li      $v0, 4
        syscall 
        j       $L0
        # END WHILE BODY
                
$L1:    
        nop     
        move    $sp, $fp
        lw      $fp, 8($sp)
        addiu   $sp, $sp, 12
        li      $v0, 10
        syscall 